from flask import Blueprint, render_template, request, flash, redirect

from project.db import (
    get_photographer_service,
    get_portfolio_by_service,
    get_single_service,
    get_types,
    get_addOns,
    add_inquiry,
)
from project.forms import InquireryForm

bp = Blueprint("main", __name__)

# views.py
from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from .db import get_clients
from .forms import VendorProfileForm, AddServiceForm

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("index.html", title="Home Page")


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
    ph_ser = get_photographer_service(photographer_service_id)
    portfolio_by_service = get_portfolio_by_service(ph_ser)
    print(portfolio_by_service)
    service = get_single_service(ph_ser.serviceId)
    types = get_types()
    addOns = get_addOns()

    # When pulldown is changed the price also chnage
    # selectedType = request.args.get("session-type")
    # quantity = request.args.get("quantity")
    # price = 0
    # price = get_details_of_type(selectedType).price * quantity

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
        portfolio=portfolio_by_service,
        service=service,
        types=types,
        addOns=addOns,
        # selectedType = selectedType,
        # price = price,
        form=form,
    )
