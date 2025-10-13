from flask import Blueprint, render_template, request, session, flash
from flask import redirect, url_for

from project.db import get_photographer_service, get_portfolio_by_service, get_single_service, get_types, get_addOns, get_single_type
from project.forms import InquireryForm

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html', title = 'Home Page')

@bp.route("/item_details/<photographer_service_id>/", methods = ["POST","GET"])
def itemDetails(photographer_service_id):
    ph_ser = get_photographer_service(photographer_service_id)
    portfolio_by_service = get_portfolio_by_service(ph_ser)
    service = get_single_service(ph_ser.serviceId)
    types = get_types()
    addOns = get_addOns()

    #When pulldown is changed the price also chnage
    # selectedType = request.args.get("session-type")
    # quantity = request.args.get("quantity")
    # price = 0
    # price = get_details_of_type(selectedType).price * quantity

    form = InquireryForm()
 
    if form.validate_on_submit():
        flash("Thank you for submitting your getting in touch.\
        We're reviewing it and will get in touch with you soon.")
    else:
        flash("Your submission failed. Please try again.", "error")
    
    return render_template(
        'item_details.html',
        portfolio = portfolio_by_service,
        service = service,
        types = types,
        addOns = addOns,
        # selectedType = selectedType,
        # price = price,
        form = form
    )