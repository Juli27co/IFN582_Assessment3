from flask import Blueprint, render_template, request, flash
from flask import redirect, url_for

from hashlib import sha256

from project.db import get_photographer, get_images_for_photographer, get_services_for_photographer, add_client, add_photographer
from project.db import check_exist_client, check_exist_photographer
from .forms import RoleForRegistration, ClientRegistrationForm, PhotographerRegistrationForm

bp = Blueprint('main', __name__)

@bp.route("/vendor_gallery/<photographer_id>/")
def vendor(photographer_id):
    photographer = get_photographer(photographer_id)
    images = get_images_for_photographer(photographer_id)
    services = get_services_for_photographer(photographer_id)
    return render_template('vendor_gallery.html', photographer = photographer, images = images, services = services)


@bp.route('/register/', methods=['GET', 'POST'])
def register_role():
    form = RoleForRegistration()
    if form.validate_on_submit():
        if form.clientSubmit.data:
            return redirect(url_for('main.register_client'))
        if form.photographerSubmit.data:
            return redirect(url_for('main.register_photographer'))
    return render_template('register.html', page="role", form=form)


@bp.route('/register/client/', methods=['POST', 'GET'])
def register_client():
    form = ClientRegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            form.password.data = sha256(form.password.data.encode()).hexdigest()
            if check_exist_client(form.email.data, form.password.data):
                flash('User already registered as a client', 'danger')
                return redirect(url_for('main.register_client'))

            add_client(form)
            flash('Thank you for your registration!', 'primary')
            return redirect(url_for('main.register_role'))

    return render_template('register.html', page='client', form=form)


@bp.route('/register/photographer/', methods=['POST', 'GET'])
def register_photographer():
    form = PhotographerRegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            form.password.data = sha256(form.password.data.encode()).hexdigest()
            if check_exist_photographer(form.email.data, form.password.data):
                flash('User already registered as a photographer', 'danger')
                return redirect(url_for('main.register_photographer'))

            add_photographer(form)
            flash('Thank you for your registration!', 'primary')
            return redirect(url_for('main.register_role'))

    return render_template('register.html', page='photographer', form=form)

