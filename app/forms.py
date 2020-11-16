from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, RadioField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import DataRequired, Email, Optional

class DetailsForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired('This field is required')], render_kw={"placeholder": "First Name", "class": "inputform"})
    last_name = StringField('Last Name', validators=[DataRequired()], render_kw={"placeholder": "Last Name"})
    email = EmailField('Email address', validators=[DataRequired(),Email('Invalid email')], render_kw={"placeholder": "john.doe@email.com"})
    personal_note = TextAreaField('Personal note', description="We will include your message in the email to the gifted person.")
    send_gift_date = DateField('Send gift on date', validators=[Optional()], description="You can select your preferred date for the gift to be sent. Please allow up to 48 hours for delivery of non-future dates.")
    subscription_options =  RadioField('Choose variant', validators=[DataRequired()], choices=[('1Y','1-year access to MyWallSt - $79.99'),('6M','6-month access to MyWallSt - $49.99')])
    submit = SubmitField('Submit')