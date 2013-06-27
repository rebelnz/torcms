from wtforms import *
from wtforms.validators import *
from wtforms.widgets import *
from datetime import date


from util import MultiValueDict

class BaseForm(Form):
  def __init__(self,handler=None,obj=None,prefix='',formdata=None,**kwargs):
    if handler:
      formdata = MultiValueDict()
      for name in handler.request.arguments.keys():
        formdata.setlist(name, handler.get_arguments(name))
    Form.__init__(self, formdata, obj=obj, prefix=prefix, **kwargs)


    
class LoginForm(BaseForm):
    email    = TextField('Email',[Required(),Email()])
    password =  PasswordField('Password',[Required()])


# class InvoiceForm(Form):
#     idate   = DateTimeField('Invoice Date*', format='%d/%m/%Y')
#     inumber = IntegerField('Invoice Number*',[
#         Required()
#     ])
#     jnumber = IntegerField('Job Number')
#     jdesc   = TextAreaField('Job Description')
#     jclient = TextField('Client - Company')
#     email   = TextField('Client Email', [
#         Length(min=6),
#         Email(message='Email address invalid.')
#     ])
#     amount = IntegerField('Amount')
#     tax    = IntegerField('Tax')
#     total  = IntegerField('Total')
#     send   = BooleanField('Send')

    # amount
    # tax
    # total
    # company
    # email
    # send

    # email = TextField('Email Address', [
    #     validators.Length(min=6),
    #     validators.Email(message='Email address invalid.')
    # ])
