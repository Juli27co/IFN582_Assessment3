# views.py
from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from .forms import VendorProfileForm, AddServiceForm  

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html', title = 'Home Page')

@bp.route('/vendor/', methods = ['POST', 'GET'])
def vendor_management():
    profile_form = VendorProfileForm(prefix = 'profile')
    service_form = AddServiceForm(prefix = 'service')

    if profile_form.validate_on_submit():
        flash("Profile changes complted", 'success')

    return render_template('vendor_management.html', title = 'Vendor Page', profile_form = profile_form, 
                           service_form = service_form)
