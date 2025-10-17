from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from project.session import add_to_cart
from project.forms import InquireryForm, LoginForm, VendorProfileForm, AddServiceForm
from flask import Blueprint, render_template, request, flash, redirect
from project.forms import InquireryForm
from project.db import (
    get_photographer_service, 
    get_portfolio_by_service, 
    get_single_service, 
    get_types,
    get_addOns, 
    add_inquiry, 
    get_single_type, 
    get_single_addOn,
    get_clients
)

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    return render_template("index.html", title="Home Page")


# test
# @bp.route('/login/')
# def login():
#     form = LoginForm()
#     return render_template('login.html', form=form)

@bp.post("/checkout/")
def checkout():
    return render_template('checkout.html')

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


@bp.route("/item_details/<photographer_service_id>/", methods = ["POST","GET"])
@bp.route("/vendor/", methods=["POST", "GET"])
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
    portfolio_by_service = get_portfolio_by_service(ph_ser)
    # get necessary information to show titles, descriptions and lists
    service = get_single_service(ph_ser.serviceId)
    types = get_types()
    addOns = get_addOns()

    # showing selected type (when it doesn't exist: None)
    selected_type_id = request.args.get("type_id")
    selectedType = get_single_type(selected_type_id)
    # showing selected addOn (when it doesn't exist: None)
    selected_addOn_id = request.args.get("addOn_id")
    selectedAddOn = get_single_addOn(selected_addOn_id)

    # caluculate price (service + type + addon) 
    price = service.price \
        + (selectedType.price if selectedType else 0) \
        + (selectedAddOn.price if selectedAddOn else 0)

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
        'item_details.html',
        pho_ser_id = photographer_service_id,
        portfolio = portfolio_by_service,
        service = service,
        types = types,
        selectedType = selectedType,
        addOns = addOns,
        selectedAddOn = selectedAddOn,
        price = price,
        form = form
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
            type_id = currentTypeId,
            addOn_id = currentAddOnId
        )
    )
