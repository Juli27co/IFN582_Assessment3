from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField,TextAreaField
from wtforms.validators import InputRequired, Email

class  InquireryForm(FlaskForm):
    """Form for item_details page."""
    fullName = StringField("Full Name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), Email()])
    phone = StringField("PhoneNumber", validators=[InputRequired()])
    message = TextAreaField("", validators=[InputRequired()])
    submit = SubmitField("Send Message")