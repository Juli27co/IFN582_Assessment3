from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField,TextAreaField, SelectField,DecimalField, RadioField, MultipleFileField
from wtforms.fields import  PasswordField
from wtforms.validators import InputRequired,Email, Optional, DataRequired, Length
from flask_wtf.file import FileField, FileAllowed


# Edit photographer form link to models and DB, also using for edit profile
class PhotographerEditForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password",)
    phone = StringField("Phone", validators=[InputRequired()])
    firstName = StringField("First name", validators=[InputRequired()])
    lastName  = StringField("Last name",  validators=[InputRequired()])
    bioDescription = TextAreaField("Bio", validators=[InputRequired(),Length(min=3, max=255)])
    location = StringField("City :",
                            render_kw={"placeholder": "Put City Name only e.g. Sydney", "rows": 1},
                            validators=[InputRequired()])
    availability = RadioField("Availability",
                               choices=[("Weekdays", "Weekdays"),("Weekends", "Weekends"),
                                         ("Short notice bookings", "Short notice bookings")],
                                         validators=[InputRequired()])
    rating = DecimalField("Rating", validators=[Optional()])
    profilePicture = FileField("Profile image", validators=[Optional(), FileAllowed(["jpg", "jpeg", "png", "gif", "webp"])])
    submit = SubmitField("Save Changes")


# Add Service and Images by Photographer
class PhotographerAddImage(FlaskForm):
    name = SelectField("Services provided", validators=[InputRequired()], choices=[], coerce=int)
    image = MultipleFileField("Up load Your Images\n You can upload multiplefiles!!!", validators=[InputRequired()])
    submit = SubmitField("Submit")
    
from wtforms.fields import (
    SubmitField,
    StringField,
    TextAreaField,
    RadioField,
    SelectMultipleField,
    DecimalField,
    SelectField,
    PasswordField,
)
from flask_wtf.file import FileField, MultipleFileField, FileAllowed
from wtforms.validators import InputRequired, Email


# Vender Edit Their Profile
class VendorProfileForm(FlaskForm):
    firstName = StringField("First Name :", validators=[InputRequired()])
    lastName = StringField("Last Name :", validators=[InputRequired()])
    phone = StringField("Phone Number :", validators=[InputRequired()])
    bio = TextAreaField(
        "Bio/Description :",
        validators=[InputRequired()],
        render_kw={
            "placeholder": "Tell clients about your style, experience, packages…",
            "rows": 4,
        },
    )
    availability = RadioField(
        "Availability :",
        choices=[
            ("Weekends", "Weekends only"),
            ("Weekdays", "Weekdays only"),
            ("Short notice bookings", "Short notice bookings"),
        ],
        validators=[InputRequired()],
    )
    location = StringField(
        "City :",
        render_kw={"placeholder": "Put City Name only e.g. Sydney", "rows": 1},
        validators=[InputRequired()],
    )
    profileImage = FileField(
        "Profile Images :",
        validators=[FileAllowed(["jpg", "jpeg", "png", "gif", "webp"], "Images only!")],
    )
    submit = SubmitField("Save Changes")


class AddServiceForm(FlaskForm):
    serviceName = StringField("Service Name :",validators=[InputRequired()],
                              render_kw={"placeholder": " e.g. Drone Photography"})
    serviceShortDescription = StringField("Short Description :",validators =[InputRequired(), Length(min=3, max=100)])
    serviceLongDescription = TextAreaField("Long Description :",render_kw={"rows": 3}, validators=[Length(min=3, max=255)])
    servicePrice = DecimalField("Price", validators=[InputRequired()])
    serviceCoverPicture = FileField("Cover image", validators=[Optional(), FileAllowed(["jpg", "jpeg", "png", "gif", "webp"])])
    serviceSubmit = SubmitField("Add New Service")


class InquireryForm(FlaskForm):
    """Form for item_details page."""

    fullName = StringField("Full Name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), Email()])
    phone = StringField("PhoneNumber", validators=[InputRequired()])
    message = TextAreaField("", validators=[InputRequired()])
    submit = SubmitField("Send Message")


class LoginForm(FlaskForm):
    """Form for login page."""
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    user_type = RadioField(
        "User Type",
        choices=[
            ("client", "Client"),
            ("photographer", "Photographer"),
            ("admin", "Admin"),
        ],
        validators=[InputRequired()],
    )
    submit = SubmitField("LOGIN")


class RegisterForm(FlaskForm):
    """Form for user registry."""

    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    firstName = StringField("Your first name", validators=[InputRequired()])
    lastName = StringField("Your surname", validators=[InputRequired()])
    phone = StringField("Your phone number", validators=[InputRequired()])
    user_type = RadioField(
        "User Type",
        choices=[("client", "Client"), ("photographer", "Photographer")],
        validators=[InputRequired()],
    )
    submit = SubmitField("Make Account")


def filters_form_choices():
    """Generate choices for filters form."""

    service_types = [
        ("Newborn Photography", "Newborn Photography"),
        ("Wedding Photography", "Wedding Photography"),
        ("Pets Photography", "Pets Photography"),
        ("Product Photography", "Product Photography"),
    ]
    availability = [
        ("Weekends", "Weekends only"),
        ("Weekdays", "Weekdays only"),
        ("Short notice bookings", "Short notice bookings"),
    ]

    locations = [
        ("Sydney", "Sydney"),
        ("Melbourne", "Melbourne"),
        ("Brisbane", "Brisbane"),
        ("Perth", "Perth"),

    ]

    return service_types, locations, availability


class FiltersForm(FlaskForm):
    """Form for filtering photographers on the index page."""

    choices = filters_form_choices()

    service_type = RadioField(
        "Service Type :", choices=choices[0]
    )
    location = RadioField("Location :", choices=choices[1])
    availability = RadioField(
        "Availability :", choices=choices[2]
    )
    submit = SubmitField("Apply Filters")
