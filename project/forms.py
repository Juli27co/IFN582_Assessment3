from flask_wtf import FlaskForm
from wtforms.fields import (
    SubmitField,
    StringField,
    TextAreaField,
    SelectField,
    DecimalField,
    RadioField,
    MultipleFileField,
)
from wtforms.fields import PasswordField
from wtforms.validators import (
    InputRequired,
    Email,
    Optional,
    DataRequired,
    Length,
    NumberRange,
)
from flask_wtf.file import FileField, FileAllowed


# Edit photographer form link to models and DB, also using for edit profile
class PhotographerEditForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField(
        "Password",
    )
    phone = StringField("Phone", validators=[InputRequired()])
    firstName = StringField("First name", validators=[InputRequired()])
    lastName = StringField("Last name", validators=[InputRequired()])
    bioDescription = TextAreaField(
        "Bio", validators=[InputRequired(), Length(min=3, max=255)]
    )
    location = StringField(
        "City :",
        render_kw={"placeholder": "Put City Name only e.g. Sydney", "rows": 1},
        validators=[InputRequired()],
    )
    availability = RadioField(
        "Availability",
        choices=[
            ("Weekdays", "Weekdays"),
            ("Weekends", "Weekends"),
            ("Short notice bookings", "Short notice bookings"),
        ],
        validators=[InputRequired()],
    )
    rating = DecimalField("Rating", validators=[Optional()])
    profilePicture = FileField(
        "Profile image",
        validators=[Optional(), FileAllowed(["jpg", "jpeg", "png", "gif", "webp"])],
    )
    submit = SubmitField("Save Changes")


# Add Service and Images by Photographer
class PhotographerAddImage(FlaskForm):
    name = SelectField(
        "Services provided", validators=[InputRequired()], choices=[], coerce=int
    )
    image = MultipleFileField(
        "Up load Your Images\n You can upload multiplefiles!!!",
        validators=[InputRequired()],
    )
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
from project.db import get_services
from project.models import Service
from wtforms.validators import NumberRange


class AddServiceForm(FlaskForm):
    serviceName = StringField(
        "Service Name :",
        validators=[InputRequired()],
        render_kw={"placeholder": " e.g. Drone Photography"},
    )
    serviceShortDescription = StringField(
        "Short Description :", validators=[InputRequired(), Length(min=3, max=100)]
    )
    serviceLongDescription = TextAreaField(
        "Long Description :", render_kw={"rows": 3}, validators=[Length(min=3, max=255)]
    )
    servicePrice = DecimalField("Price", validators=[InputRequired()])
    serviceCoverPicture = FileField(
        "Cover image",
        validators=[Optional(), FileAllowed(["jpg", "jpeg", "png", "gif", "webp"])],
    )
    serviceSubmit = SubmitField("Add New Service")


class AddTypeForm(FlaskForm):
    typeName = StringField("Type Name", validators=[InputRequired(), Length(max=100)])
    shortDescription = TextAreaField(
        "Short Description", validators=[InputRequired(), Length(max=255)]
    )
    price = DecimalField("Price", validators=[DataRequired()])
    submit = SubmitField("Add Type")


class AddOnForm(FlaskForm):
    addOn = StringField("Add-On Name", validators=[DataRequired(), Length(max=255)])
    price = DecimalField("Price", validators=[DataRequired()])
    submit = SubmitField("Save Add-On")


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


availability_choices = [
    ("Weekends", "Weekends only"),
    ("Weekdays", "Weekdays only"),
    ("Short notice bookings", "Short notice bookings"),
]

location_choices = [
    ("Sydney", "Sydney"),
    ("Melbourne", "Melbourne"),
    ("Brisbane", "Brisbane"),
    ("Perth", "Perth"),
]


class FiltersForm(FlaskForm):
    """Form for filtering photographers on the index page."""

    service_type = RadioField("Service Type :", choices=[])
    location = RadioField("Location :", choices=location_choices)
    availability = RadioField("Availability :", choices=availability_choices)
    min_rating = DecimalField(
        "Minimum Rating :",
        places=1,
        validators=[InputRequired(), NumberRange(min=0, max=5)],
        render_kw={"min": 0, "max": 5, "type": "range", "step": "0.1"},
        default=0.0,
    )
    submit = SubmitField("Apply Filters")


class SearchForm(FlaskForm):
    """Form for searching photographers on the index page."""

    search_query = StringField(
        "Search Photographers",
        validators=[Optional(), Length(min=1, max=100)],
        render_kw={"placeholder": "Enter photographer name..."},
    )
    submit = SubmitField("Search")
