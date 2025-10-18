from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from project.models import User
from project.session import add_to_cart
from project.forms import (
    InquireryForm,
    LoginForm,
    VendorProfileForm,
    AddServiceForm,
    RegisterForm,
    FiltersForm,
)
from hashlib import sha256

from project.forms import InquireryForm
from project.db import (
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
)
from project.wrappers import only_photographers

bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET", "POST"])
def index():
    form = FiltersForm()

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

        print(f"Redirecting with query params: {query_params}")
        return redirect(url_for("main.index", **query_params))

    # Handle GET request with query parameters
    if request.method == "GET":
        # Get filters from query parameters
        service_type = request.args.get("service_type")
        location = request.args.get("location")
        availability = request.args.get("availability")

        if service_type:
            filters["service_type"] = service_type
            form.service_type.data = service_type
        if location:
            filters["location"] = location
            form.location.data = location
        if availability:
            filters["availability"] = availability
            form.availability.data = availability

        print(f"Query params filters: {filters}")

        if filters:
            flash("Filters applied!", "success")

    # Fetch photographers with filters
    photographers = get_photographers(filters)
    print(f"Number of photographers found: {len(photographers)}")

    return render_template(
        "index.html", title="Home Page", form=form, photographers=photographers
    )


@bp.post("/checkout/")
def checkout():
    return render_template("checkout.html")


# Add item to session
@bp.post("/cart/")
def adding_to_cart():
    # get item information from request
    phSerId = request.form.get("photographer_service_id")
    serviceId = request.form.get("serviceId")
    typeId = request.form.get("typeId")
    addOnId = request.form.get("addOnId")
    # handle the case when type is not selected.(type is requierd)
    if typeId == "":
        flash("Please select a session type before adding to cart.", "error")
        return redirect(url_for("main.itemDetails", photographer_service_id=phSerId))
    # handle the case when addOn is not selected (addon is optional)
    if addOnId == "":
        addOnId = "None"

    add_to_cart(serviceId, typeId, addOnId)
    flash("Your items have been added to your cart!")
    return redirect(url_for("main.itemDetails", photographer_service_id=phSerId))


@bp.route("/vendor/", methods=["POST", "GET"])
@only_photographers
def vendor_management():
    profile_form = VendorProfileForm(prefix="profile")
    service_form = AddServiceForm(prefix="service")

    if profile_form.validate_on_submit():
        flash("Profile changes complted", "success")

    return render_template(
        "vendor_management.html",
        title="Vendor Page",
        profile_form=profile_form,
        service_form=service_form,
    )


@bp.route("/item_details/<photographer_service_id>/", methods=["POST", "GET"])
def itemDetails(photographer_service_id):
    # get images associated with selected photographer and service
    ph_ser = get_photographer_service(photographer_service_id)
    images_by_ph_ser = get_images_by_photographer_service(ph_ser)
    # get necessary information to show titles, descriptions and lists
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
    price = (
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
        service=service,
        types=types,
        selectedType=selectedType,
        addOns=addOns,
        selectedAddOn=selectedAddOn,
        price=price,
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
            elif form.user_type.data == "photographer":
                user = check_for_photographer(email, password)
            elif form.user_type.data == "admin":
                user = check_for_admin(email, password)
            if not user:
                flash("Invalid username or password", "error")
                return redirect(url_for("main.login"))
            # Store full user info in session
            session["user"] = user
            session["logged_in"] = True
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
