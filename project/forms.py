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
    name = SelectField("Services provided", validate_choice=[InputRequired()], choices=[], coerce=int)
    image = MultipleFileField("Up load Your Images\n You can upload multiplefiles!!!", validators=[InputRequired()])
    submit = SubmitField("Submit")


