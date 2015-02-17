from flask.ext.wtf import Form
from wtforms.fields import *
from wtforms.validators import Required

class ContactForm(Form):
  name = TextField("Name")
  email = TextField("Email")
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")