# views.py
from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    current_app,
    url_for,
    session,
)
from hashlib import sha256
import os
from werkzeug.utils import secure_filename

# Form imports
from .forms import (
    PhotographerEditForm,
    PhotographerAddImage,
    AddServiceForm,
    AddTypeForm,
    AddOnForm,
    InquireryForm,
    LoginForm,
    RegisterForm,
    FiltersForm,
    CheckoutForm
)

# Database function imports
from .db import (
    get_photographer,
    add_or_update_photographer,
    get_photographer_management,
    get_services_for_photographer,
    get_all_services,
    insert_image,
    ensure_photographer_service,
    get_images_for_photographer,
    delete_image_row,
    admin_insert_service,
    get_services,
    admin_add_type,
    admin_add_addon,
    admin_delete_service,
    admin_delete_type,
    admin_delete_addon,
    add_inquiry,
    add_user,
    check_for_admin,
    check_for_client,
    check_for_photographer,
    get_addOns,
    get_clients,
    get_images_by_photographer_service,
    get_photographer_service,
    get_photographers,
    get_single_addOn,
    get_single_service,
    get_single_type,
    get_types,
    insert_order_detail
)

# Session and wrapper imports
from project.session import add_to_cart, get_cart, remove_cart_item
from project.wrappers import only_photographers, only_admins

bp = Blueprint("main", __name__)


def save_image(file_storage):
    if not file_storage or file_storage.filename == "":
        return None
    filename = secure_filename(os.path.basename(file_storage.filename))
    upload_dir = current_app.config["UPLOAD_FOLDER"]
    os.makedirs(upload_dir, exist_ok=True)

    dest = os.path.join(upload_dir, filename)
    i = 1
    base, ext = os.path.splitext(filename)
    while os.path.exists(dest):
        filename = f"{base}_{i}{ext}"
        dest = os.path.join(upload_dir, filename)
        i += 1
    file_storage.save(dest)
    return filename


@bp.route("/checkout/", methods=["GET", "POST"])
def checkout():
    cart = get_cart()
    return render_template("checkout.html", cart=cart, total_cost=cart.total_cost())


@bp.post("/cart/remove/")
def cart_remove():
    item_id = request.form.get("item_id")
    cart = get_cart()
    item = cart.get_item(item_id)

    if item:
        flash("Your item has been removed from your cart.")
        remove_cart_item(item_id)
    else:
        flash("Item not found in basket.", "warning")

    return redirect(url_for("main.checkout"))


@bp.route("/vendor/<int:photographer_id>", methods=["POST", "GET"])
# @only_photographers
def vendor_management(photographer_id):
    form = PhotographerEditForm(prefix="EditProfile")

    if request.method == "GET":
        row = get_photographer_management(photographer_id)
        if row:
            form.email.data = row["email"]
            form.phone.data = row["phone"]
            form.firstName.data = row["firstName"]
            form.lastName.data = row["lastName"]
            form.bioDescription.data = row["bioDescription"]
            form.location.data = row["location"]
            form.availability.data = row["availability"]
            form.rating.data = row["rating"]
        else:
            flash("Photographer not found", "warning")

    if form.validate_on_submit():
        image_filename = None
        if form.profilePicture.data:
            image_filename = save_image(form.profilePicture.data)

        saved_id = add_or_update_photographer(
            form, photographer_id=photographer_id, image_filename=image_filename
        )
        flash("Your changes completed!!", "success")
        return redirect(url_for("main.vendor_management", photographer_id=saved_id))

    row = get_photographer_management(photographer_id)
    vendor_name = None
    bio = None
    profile_image = None
    if row:
        vendor_name = f"{row['firstName']} {row['lastName']}".strip()
        bio = row["bioDescription"]
        profile_image = row["profilePicture"]

    return render_template(
        "vendor_management.html",
        title="Vendor Page",
        form=form,
        vendor_name=vendor_name,
        profile_image=profile_image,
        bio=bio,
        photographer_id=photographer_id,
    )


@bp.route("/vendor/management/", methods=["GET"])
# @only_photographers
def vendor_management_check():
    if session.get("userType") != "photographer":
        flash("Please log in as a photographer.", "error")
        return redirect(url_for("main.login"))

    vendor = session.get("photographer_id")
    if not vendor:
        flash("Photographer ID missing.", "error")
        return redirect(url_for("main.login"))

    return redirect(url_for("main.vendor_management", photographer_id=vendor))


@bp.route("/vendor/add-images/<int:photographer_id>/", methods=["GET", "POST"])
# @only_photographers
def add_images_photographer(photographer_id):
    form = PhotographerAddImage()

    services = get_all_services()
    form.name.choices = [(int(s["id"]), s["name"]) for s in services]

    if form.validate_on_submit():
        service_id = form.name.data
        ensure_photographer_service(photographer_id, service_id)

        for fs in form.image.data:
            filename = save_image(fs)
            if filename:
                image_relative_path = filename
                image_description = os.path.splitext(filename)[0]
                insert_image(
                    service_id, photographer_id, image_relative_path, image_description
                )

        flash("Uploaded successfully!", "success")
        return redirect(
            url_for("main.add_images_photographer", photographer_id=photographer_id)
        )

    images = get_images_for_photographer(photographer_id)
    return render_template(
        "add_service.html",
        form=form,
        photographer_id=photographer_id,
        services=services,
        images=images,
    )


@bp.post("/vendor/<int:photographer_id>/images/<int:image_id>/delete")
# @only_photographers
def delete_image(photographer_id, image_id):
    # to delete the images of photographer by photographer_id
    deleted = delete_image_row(image_id, photographer_id)
    if deleted == 1:
        flash("Image deleted.", "success")
    else:
        flash("Cannot delete this image (not found).", "danger")
    return redirect(
        url_for("main.add_images_photographer", photographer_id=photographer_id)
    )


@bp.route("/", methods=["GET", "POST"])
def index():

    all_services = get_all_services()
    form = FiltersForm()
    form.service_type.choices = [
        (int(service["id"]), service["name"]) for service in all_services
    ]

    # Initialize filters dictionary
    filters = {}

    if request.method == "POST" and form.validate_on_submit():
        # Extract filter values from form and redirect with query params
        query_params = {}

        if form.service_type.data:
            query_params["service_type"] = form.service_type.data
        if form.location.data:
            query_params["location"] = form.location.data
        if form.availability.data:
            query_params["availability"] = form.availability.data
        if form.min_rating.data is not None:
            query_params["min_rating"] = str(form.min_rating.data)

        print(f"Redirecting with query params: {query_params}")
        return redirect(url_for("main.index", **query_params))

    # Handle GET request with query parameters
    if request.method == "GET":
        # Get filters from query parameters
        service_type = request.args.get("service_type")
        location = request.args.get("location")
        availability = request.args.get("availability")
        min_rating = request.args.get("min_rating")
        search_query = request.args.get("search")

        if service_type:
            filters["service_type"] = service_type
            form.service_type.data = service_type
        if location:
            filters["location"] = location
            form.location.data = location
        if availability:
            filters["availability"] = availability
            form.availability.data = availability
        if min_rating:
            filters["min_rating"] = float(min_rating)
            form.min_rating.data = float(min_rating)
        if search_query:
            filters["search"] = search_query

        print(f"Query params filters: {filters}")

        if filters:
            flash("Filters applied!", "success")

    # Fetch photographers with filters
    photographers = get_photographers(filters)
    print(f"Number of photographers found: {len(photographers)}")

    return render_template(
        "index.html", title="Home Page", form=form, photographers=photographers
    )


# Add item to session
@bp.post("/cart/")
def adding_to_cart():
    # get item information from request
    phSerId = request.form.get("photographer_service_id")
    pho_id = request.form.get("photographer_id")
    serviceId = request.form.get("serviceId")
    typeId = request.form.get("typeId")
    addOnId = request.form.get("addOnId")
    subtotal = request.form.get("subtotal")
    # handle the case when type is not selected.(type is requierd)
    if typeId == "":
        flash("Please select a session type before adding to cart.", "error")
        return redirect(url_for("main.itemDetails", photographer_service_id=phSerId))
    # handle the case when addOn is not selected (addon is optional)
    if addOnId == "":
        addOnId = "None"

    add_to_cart(serviceId, pho_id, typeId, addOnId, subtotal)
    flash("Your items have been added to your cart!")
    return redirect(url_for("main.itemDetails", photographer_service_id=phSerId))


@bp.route("/item_details/<photographer_service_id>/", methods=["POST", "GET"])
def itemDetails(photographer_service_id):
    # get images associated with selected photographer and service
    ph_ser = get_photographer_service(photographer_service_id)
    images_by_ph_ser = get_images_by_photographer_service(ph_ser)
    # get necessary information to show titles, descriptions and lists
    photographer = get_photographer(ph_ser.photographer_id)
    service = get_single_service(ph_ser.service_id)
    types = get_types()
    addOns = get_addOns()
    # showing selected type (when it doesn't exist: None)
    selected_type_id = request.args.get("type_id")
    selectedType = get_single_type(selected_type_id)
    # showing selected addOn (when it doesn't exist: None)
    selected_addOn_id = request.args.get("addOn_id")
    selectedAddOn = get_single_addOn(selected_addOn_id)

    # caluculate price (service + type + addon)
    subtotal = (
        service.price
        + (selectedType.price if selectedType else 0)
        + (selectedAddOn.price if selectedAddOn else 0)
    )

    # handle inquirery form
    # When the form does not have error, the data is stored into Inquiry table.
    form = InquireryForm()
    if request.method == "POST":
        if form.validate_on_submit():
            add_inquiry(form)
            flash(
                "Thank you for submitting a form.\
            We're reviewing it and will get in touch with you soon."
            )
            return redirect(request.url)
        else:
            flash("Your submission failed. Please try again.", "error")

    return render_template(
        "item_details.html",
        pho_ser_id=photographer_service_id,
        images=images_by_ph_ser,
        photographer=photographer,
        service=service,
        types=types,
        selectedType=selectedType,
        addOns=addOns,
        selectedAddOn=selectedAddOn,
        subtotal=subtotal,
        form=form,
    )


@bp.post("/item_details/<photographer_service_id>/selectOption/")
def selectOption(photographer_service_id):

    # currentTypeId = selected type: It updates when the dropdown changes.
    currentTypeId = request.args.get("type_id")
    newTypeId = request.form.get("form-type")
    if newTypeId:
        currentTypeId = newTypeId

    # currentAddOnId = selected addOn: It updates when the radiobutton is checked.
    currentAddOnId = request.args.get("addOn_id")
    newAddOnId = request.form.get("form-addOn")

    # uncheck the addOn checkbox when you click selected one again.
    if newAddOnId:
        if currentAddOnId == newAddOnId:
            currentAddOnId = ""
        else:
            currentAddOnId = newAddOnId

    return redirect(
        url_for(
            "main.itemDetails",
            photographer_service_id=photographer_service_id,
            type_id=currentTypeId,
            addOn_id=currentAddOnId,
        )
    )


@bp.route("/login/", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            email = form.email.data
            password = sha256(form.password.data.encode()).hexdigest()

            if form.user_type.data == "client":
                user = check_for_client(email, password)
                userType = "client"
            elif form.user_type.data == "photographer":
                user = check_for_photographer(email, password)
                userType = "photographer"
            elif form.user_type.data == "admin":
                user = check_for_admin(email, password)
                userType = "admin"
            if not user:
                flash("Invalid username or password", "error")
                return redirect(url_for("main.login"))
            # Store full user info in session
            session["user"] = user
            session["userType"] = userType
            session["logged_in"] = True
            if userType == "photographer":
                session["photographer_id"] = int(user.id)
            flash("Login successful!")
            return redirect(url_for("main.index"))
    return render_template("login.html", form=form)


@bp.route("/register/", methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            # Add the new user to the database
            add_user(form)
            flash("Registration successful! You can now log in.", "success")
            return redirect(url_for("main.login"))
        except Exception as e:
            # Handle potential database errors (e.g., duplicate email/username)
            flash("Registration failed. Email or username may already exist.", "error")
            print(f"Registration error: {e}")
    return render_template("register.html", form=form)


@bp.route("/logout/")
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("main.index"))


@bp.route("/vendor_gallery/<photographer_id>/")
def vendor(photographer_id):
    photographer = get_photographer(photographer_id)
    images = get_images_for_photographer(photographer_id)
    services = get_services_for_photographer(photographer_id)
    vendorProfile = get_photographer_management(photographer_id)

    return render_template(
        "vendor_gallery.html",
        photographer=photographer,
        images=images,
        services=services,
        vendorProfile=vendorProfile,
    )


# functions about admin management: add and delete servcie, session, and add-om


@bp.route("/admin/manage/", methods=["GET"])
@only_admins
def admin_management():
    services = get_services()
    types = get_types()
    addons = get_addOns()
    return render_template(
        "admin_manage.html",
        serviceForm=AddServiceForm(prefix="service"),
        typeForm=AddTypeForm(prefix="type"),
        addonForm=AddOnForm(prefix="addon"),
        services=services,
        types=types,
        addons=addons,
    )


@bp.post("/admin/manage/service/")
def add_new_service():
    serviceForm = AddServiceForm(prefix="service")
    typeForm = AddTypeForm(prefix="type")
    addonForm = AddOnForm(prefix="addon")

    if serviceForm.validate_on_submit():
        name = serviceForm.serviceName.data
        short = serviceForm.serviceShortDescription.data
        long = serviceForm.serviceLongDescription.data
        price = float(serviceForm.servicePrice.data)

        coverImage = None
        file = serviceForm.serviceCoverPicture.data
        if file:
            coverImage = save_image(file)

        admin_insert_service(name, short, long, price, coverImage)
        flash("Service added!", "success")
        return redirect(url_for("main.admin_management"))

    services = get_services()
    types = get_types()
    addons = get_addOns()

    flash("Please fill the Service form", "error")
    return render_template(
        "admin_manage.html",
        serviceForm=serviceForm,
        typeForm=typeForm,
        addonForm=addonForm,
        services=services,
        types=types,
        addons=addons,
    )


@bp.post("/admin/manage/type")
def add_new_type():
    typeForm = AddTypeForm(prefix="type")
    serviceForm = AddServiceForm(prefix="service")
    addonForm = AddOnForm(prefix="addon")

    if typeForm.validate_on_submit():
        name = typeForm.typeName.data
        short = typeForm.shortDescription.data
        price = float(typeForm.price.data)

        admin_add_type(name, short, price)
        flash("Service Type Added!", "success")
        return redirect(url_for("main.admin_management"))

    services = get_services()
    types = get_types()
    addons = get_addOns()

    flash("Please fill the Type form", "error")
    return render_template(
        "admin_manage.html",
        serviceForm=serviceForm,
        typeForm=typeForm,
        addonForm=addonForm,
        services=services,
        types=types,
        addons=addons,
    )


@bp.post("/admin/manage/addon")
def add_new_addon():
    addonForm = AddOnForm(prefix="addon")
    serviceForm = AddServiceForm(prefix="service")
    typeForm = AddTypeForm(prefix="type")

    if addonForm.validate_on_submit():
        name = addonForm.addOn.data
        price = float(addonForm.price.data)

        admin_add_addon(name, price)
        flash("Add-On Added!", "success")
        return redirect(url_for("main.admin_management"))

    services = get_services()
    types = get_types()
    addons = get_addOns()

    flash("Please fill the Add-on Form", "error")
    return render_template(
        "admin_manage.html",
        serviceForm=serviceForm,
        typeForm=typeForm,
        addonForm=addonForm,
        services=services,
        types=types,
        addons=addons,
    )


@bp.post("/admin/manage/service/delete")
def delete_service():
    service_id = request.form.get("service_id", type=int)
    if not service_id:
        flash("Invalid service id", "error")
        return redirect(url_for("main.admin_management"))

    deleted = admin_delete_service(service_id)
    if deleted:
        flash("Service deleted", "success")
    else:
        flash("Cannot delete: service is not found", "error")
    return redirect(url_for("main.admin_management"))


@bp.post("/admin/manage/type/delete")
def delete_type():
    type_id = request.form.get("type_id", type=int)
    if not type_id:
        flash("Invalid type id", "error")
        return redirect(url_for("main.admin_management"))

    deleted = admin_delete_type(type_id)
    if deleted:
        flash("Session type deleted", "success")
    else:
        flash("Cannot delete: session type is not found", "error")
    return redirect(url_for("main.admin_management"))


@bp.post("/admin/manage/addon/delete")
def delete_addon():
    addon_id = request.form.get("addon_id", type=int)
    if not addon_id:
        flash("Invalid add-on id", "error")
        return redirect(url_for("main.admin_management"))

    deleted = admin_delete_addon(addon_id)
    if deleted:
        flash("Add-on deleted", "success")
    else:
        flash("Cannot delete: add-on is not found", "error")
    return redirect(url_for("main.admin_management"))

@bp.route('/client/checkout/', methods=['GET', 'POST'])
def orderCheckout():
    form = CheckoutForm()
    user = session.get("user")

    if request.method == 'GET' and user:
        form.full_name.data = f"{user['firstName']} {user['lastName']}"
        form.email.data = user['email']
        form.phone.data = user['phone']

    if request.method == 'POST':
        if not user:
            flash("Please log in before placing your order.", "error")
            return redirect(url_for("main.login"))

        client_id = user["id"]
        address = form.address.data
        payment_method = form.payment_method.data
        insert_order_detail(client_id, address, payment_method)
        flash("Your booking has been set to company successfully! Our staff will contact you shortly.", "success")
        return redirect(url_for('main.orderCheckout'))

    readonly = 'user' in session
    return render_template("checkout.html", form=form, user=user, readonly=readonly)