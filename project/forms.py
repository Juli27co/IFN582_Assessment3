from flask_wtf import FlaskForm
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


# vendor add their servcies
class AddServiceForm(FlaskForm):
    serviceName = SelectField(
        "Service Name :",
        choices=[
            ("Newborn Photography", "Newborn Photography"),
            ("Wedding Photography", "Wedding Photography"),
            ("Pets Photography", "Pets Photography"),
            ("Product Photography", "Product Photography"),
        ],
        validators=[InputRequired()],
    )
    serviceShortDescription = StringField(
        "Short Description :", validators=[InputRequired()]
    )
    serviceLongDescription = TextAreaField("Long Description :", render_kw={"rows": 3})
    servicePrice = DecimalField("Price :", validators=[InputRequired()])
    serviceImage = MultipleFileField(
        "Portfolio / Service Images :",
        validators=[FileAllowed(["jpg", "jpeg", "png", "gif", "webp"], "Images only!")],
    )
    serviceSubmit = SubmitField("Add Service!")


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
