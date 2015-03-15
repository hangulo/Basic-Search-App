from flask.ext.wtf import Form
from wtforms.fields import *
from wtforms.validators import Required

class ContactForm(Form):
  name = TextField("Name")
  email = TextField("Email")
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")

class SearchForm(Form):
  subdomain = TextField("FQDN", default="sample.loggly.com")
  user = TextField("User:", default="hector")
  password = TextField("Password:", default="hector")
  searchFrom = TextField("From:", default="-10m")
  searchTo = TextField("To:", default="now")
  query = TextField("Search Query:", default="*")
  size = TextField("# of Results to Show", default="1")
  submit = SubmitField("Search")


class AnalyzeForm(Form):
    message = TextAreaField("Input JSON")
    submit = SubmitField("Analyze Me!")