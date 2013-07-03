import tornado.web
import forms
import db
from time import strftime

from pprint import pprint


class Form(tornado.web.UIModule):
  """
  Generic form rendering module. Works with wtforms.
  Use this in your template code as:
  {% module Form(form) %}
  where `form` is a wtforms.Form object. Note that this module does not render
  <form> tag and any buttons.
  """

  def render(self, form):
    """docstring for render"""
    return self.render_string('uimodules/form.html', form=form)


class NavModule(tornado.web.UIModule):
    def render(self):
        return self.render_string('uimodules/nav.html')



# #embed map/listing edit js only if we need it
#   def javascript_files(self):
#     js_scripts = ['http://maps.googleapis.com/maps/api/js?\
# key=<apikey>&sensor=true',
#                   '/static/js/listing_edit.js']
#     return js_scripts


# class ListingDetailModule(tornado.web.UIModule):
#   def render(self,listing):
#     return self.render_string('uimodules/detail.html',listing=listing)


# class HomepageListingDetailModule(tornado.web.UIModule):
#   def render(self,listing):
#     return self.render_string('uimodules/homepage_detail.html',listing=listing)

# class SuperListingDetailModule(tornado.web.UIModule):
#   def render(self,listing):
#     return self.render_string('uimodules/super_detail.html',listing=listing)

#   def css_files(self):
#     return "/static/css/super.css"
