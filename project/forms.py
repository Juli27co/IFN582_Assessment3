from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField,TextAreaField,RadioField, SelectMultipleField, DecimalField, SelectField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, MultipleFileField, FileAllowed


# Vender Edit Their Profile 
class VendorProfileForm(FlaskForm):
    firstName = StringField("First Name :", validators=[InputRequired()])
    lastName = StringField("Last Name :", validators=[InputRequired()])
    phone = StringField("Phone Number :", validators=[InputRequired()])
    bio = TextAreaField("Bio/Description :", validators=[InputRequired()],
                      render_kw={"placeholder": "Tell clients about your style, experience, packages…", "rows": 4})
    availability = RadioField("Availability :",
                              choices=[("Weekends", "Weekends only"), ("Weekdays", "Weekdays only"), ("Short notice bookings", "Short notice bookings")],
                               validators=[InputRequired()])
    location = StringField("City :",
                           render_kw={"placeholder": "Put City Name only e.g. Sydney", "rows": 1},
                           validators=[InputRequired()])
    profileImage = FileField("Profile Images :",
                             validators=[FileAllowed(["jpg", "jpeg", "png", "gif", "webp"], "Images only!")])
    submit = SubmitField("Save Changes") 


# vendor add their servcies                                                                                               
class AddServiceForm(FlaskForm):
    serviceName = SelectField("Service Name :", 
                               choices=[("Newborn Photography", "Newborn Photography"),("Wedding Photography", "Wedding Photography"),("Pets Photography", "Pets Photography"), ("Product Photography","Product Photography")],
                               validators=[InputRequired()])
    serviceShortDescription = StringField("Short Description :",validators =[InputRequired()])
    serviceLongDescription = TextAreaField("Long Description :",render_kw={"rows": 3})
    servicePrice = DecimalField("Price :",validators=[InputRequired()])
    serviceImage = MultipleFileField("Portfolio / Service Images :",
                               validators=[FileAllowed(["jpg", "jpeg", "png", "gif", "webp"], "Images only!")])
    serviceSubmit = SubmitField("Add Service!")
                         



