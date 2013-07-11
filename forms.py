from wtforms import *
from wtforms.validators import *
from wtforms.widgets import *
from datetime import date
import pytz

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


class AdminSettingsSiteForm(BaseForm):
  sitename  = TextField(u'Site Name*',[Required()])
  contact   = TextField(u'Contact*',[Required()])
  tagline   = TextField(u'Tag Line')
  timezone  = SelectField('Timezone',
        choices = [(tz, tz) for tz in pytz.common_timezones],
        coerce=unicode, description="Timezone"
    )

class AdminSettingsAddressForm(BaseForm):
  address = TextField(u'Address*',[Required()])
  suburb  = TextField(u'Suburb')
  city    = TextField(u'City')
  zipcode = TextField(u'Zip Code*',[Required()])


class AdminSettingsSocialForm(BaseForm):
  facebook = TextField(u'Facebook')
  googleplus  = TextField(u'Google+')
  kakao    = TextField(u'Kakao')
  twitter = TextField(u'Twitter')
  linkedin = TextField(u'Linkedin')


class AdminPagesForm(BaseForm):
  title = TextField(u'Title*',[Required()])
  subtitle  = TextField(u'Heading')
  content  = TextAreaField()
  # kakao    = TextField(u'Kakao')
  # twitter = TextField(u'Twitter')
  # linkedin = TextField(u'Linkedin')
  
