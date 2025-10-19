# views.py
from flask import Blueprint, render_template, request, flash, redirect, current_app, url_for
from .forms import PhotographerEditForm, PhotographerAddImage
from .db import get_photographer, add_or_update_photographer
from .db import get_all_services, insert_image, ensure_photographer_service, get_images_for_photographer, delete_image_row
import os
from werkzeug.utils import secure_filename




bp = Blueprint('main', __name__)

def save_image(file_storage):
    if not file_storage or file_storage.filename == '':
        return None
    filename = secure_filename(os.path.basename(file_storage.filename))
    upload_dir = current_app.config['UPLOAD_FOLDER'] 
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

@bp.route('/')
def index():
    return render_template('index.html', title = 'Home Page')


@bp.route('/photographer/<int:photographer_id>', methods = [ 'POST', 'GET'])
# @login_required
# @photographer_required
def vendor_management(photographer_id):
    form = PhotographerEditForm(prefix = 'EditProfile')

    if request.method == 'GET':
        row = get_photographer(photographer_id)
        if row:
            form.email.data = row['email']        
            form.phone.data = row['phone']
            form.firstName.data = row['firstName']
            form.lastName.data = row['lastName']
            form.bioDescription.data = row['bioDescription']
            form.location.data = row['location']
            form.availability.data = row['availability']
            form.rating.data = row['rating']
    
    if form.validate_on_submit():
        image_filename = None
        if form.profilePicture.data:
            image_filename = save_image(form.profilePicture.data)
        
        saved_id = add_or_update_photographer(form, photographer_id=photographer_id, image_filename=image_filename)
        flash("Your changes completed!!", 'success')
        return redirect(url_for('main.vendor_management', photographer_id=saved_id))

    row = get_photographer(photographer_id)
    vendor_name = None
    bio = None
    profile_image = None
    if row:
        vendor_name = f"{row['firstName']} {row['lastName']}".strip()
        bio = row['bioDescription']
        profile_image = row['profilePicture']  
        
    return render_template('vendor_management.html',title='Vendor Page',form=form, vendor_name = vendor_name, 
                           profile_image = profile_image, bio = bio, photographer_id=photographer_id)


@bp.route("/photographer/add-images/<int:photographer_id>/", methods=["GET", "POST"])
# @login_required
# @photographer_required
def add_images_photographer(photographer_id):
    form = PhotographerAddImage()

    services = get_all_services()
    form.name.choices = [(s["id"], s["name"]) for s in services]

    if form.validate_on_submit():
        service_id = form.name.data
        ensure_photographer_service(photographer_id, service_id)

        for fs in form.image.data:
            filename = save_image(fs) 
            if filename:
                image_relative_path = f"img/{filename}"
                image_description  = os.path.splitext(filename)[0]
                insert_image(service_id, photographer_id, image_relative_path, image_description)

        flash("Uploaded successfully!", "success")
        return redirect(url_for("main.add_images_photographer", photographer_id=photographer_id))
    
    images = get_images_for_photographer(photographer_id)
    
    return render_template("add_service.html", form=form, photographer_id=photographer_id, services = services, images = images)


@bp.post("/photographer/<int:photographer_id>/images/<int:image_id>/delete")
# @login_required
# @photographer_required
def delete_image(photographer_id, image_id):
    # to delete the images of photographer by photographer_id
    deleted = delete_image_row(image_id, photographer_id)
    if deleted == 1:
        flash("Image deleted.", "success")
    else:
        flash("Cannot delete this image (not found).", "danger")
    return redirect(url_for("main.add_images_photographer", photographer_id=photographer_id))