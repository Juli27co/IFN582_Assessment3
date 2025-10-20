from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, PasswordField, RadioField
from wtforms.validators import InputRequired, Email


class RoleForRegistration(FlaskForm):
    clientSubmit = SubmitField("Create Client Account")
    photographerSubmit = SubmitField("Create Photographer Account")



class ClientRegistrationForm(FlaskForm):
    email = StringField("Email", validators= [InputRequired(), Email()])
    password = PasswordField("Password", validators= [InputRequired()])
    phone = StringField("Your telephone number", validators= [InputRequired()])
    firstName = StringField("Your first name", validators= [InputRequired()])
    lastName = StringField("Your last name", validators= [InputRequired()])
    preferredPaymentMethod = RadioField("Payment Method", choices = [("Cash", "Cash"), ("Credit card", "Credit card")], validators= [InputRequired()])
    address = StringField("Your address", validators = [InputRequired()])
    submit = SubmitField("Register")



class PhotographerRegistrationForm(FlaskForm):
    email = StringField("Email", validators= [InputRequired(), Email()])
    password = PasswordField("Password", validators= [InputRequired()])
    phone = StringField("Your telephone number", validators= [InputRequired()])
    firstName = StringField("Your first name", validators= [InputRequired()])
    lastName = StringField("Your last name", validators= [InputRequired()])
    location = StringField("Your location", validators= [Optional()])
    submit = SubmitField("Register")

class CheckoutForm(FlaskForm):
    full_name = StringField("Full name", validators=[InputRequired(), Length(min=2, max=100)])
    email = StringField("Email", validators=[InputRequired(), Email()])
    phone = StringField("PhoneNumber", validators=[InputRequired()])
    address = StringField("Address", validators=[InputRequired()])
    payment_method = RadioField(
        "Payment Method",
        choices=[("cash", "Cash"), ("credit card", "Credite card")],
        validators=[InputRequired()],
    )
    checkout_submit = SubmitField("Checkout")
