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


class AdminSideNavModule(tornado.web.UIModule):
    def render(self):
        return self.render_string('admin/uimodules/admin_side_nav.html')


class AdminTopNavModule(tornado.web.UIModule):
    def render(self):
        # to set active class + we can add new items to nav
        nav_items = (
            ("/admin","Admin","icon-lock"),
            ("/admin/settings/site","Settings","icon-cog"), #need url for default
            ("/admin/users","Users","icon-user"),
            ("/admin/messages","Messages","icon-inbox"),
            ("/","View Site","icon-eye-open")
            )


        return self.render_string('admin/uimodules/admin_top_nav.html',
                                  items = nav_items)


class AdminSettingsNavModule(tornado.web.UIModule):
    def render(self):
        nav_items = (
            ("/admin/settings/site","Site"),
            ("/admin/settings/analytics","Analytics"),
            ("/admin/settings/data","Data"),
            ("/admin/settings/campaign","Campaign"),
            ("/admin/settings/calendar","Calendar"),
            ("/admin/settings/map","Map"),
            )

        return self.render_string('admin/uimodules/admin_settings_nav.html',
                                  items = nav_items)

    # def javascript_files(self):
    #     return "/static/js/admin-settings.js"


class AdminSettingsSiteFormModule(tornado.web.UIModule):
    def render(self):
        data = db.get_site_settings()
        if data:
            form = forms.AdminSettingsSiteForm(
                sitename=data["sitename"],
                contact=data["contact"],
                tagline=data["tagline"],
                timezone=data["timezone"]
                )
        else:
            form = forms.AdminSettingsSiteForm() # from forms file
        return self.render_string('admin/forms/admin_settings_site_form.html',
                                  form=form,
                                  )

class AdminSettingsSiteModule(tornado.web.UIModule):
    def render(self):
        # get map data too?
        data = db.get_site_settings()
        if data:
            # settings["updated"] = strftime("%a, %d %b %Y %H:%M:%S +0000",data["updated"])
            settings = data
        else:
            settings = False
        return self.render_string('admin/uimodules/admin_settings_site.html',
                                  settings=settings,
                                  )


class AdminSettingsCalendarModule(tornado.web.UIModule):
    def render(self):
        return self.render_string('admin/uimodules/admin_settings_calendar.html')


class AdminSettingsCampaignModule(tornado.web.UIModule):
    def render(self):
        return self.render_string('admin/uimodules/admin_settings_campaign.html')


class AdminSettingsDataModule(tornado.web.UIModule):
    def render(self):
        return self.render_string('admin/uimodules/admin_settings_data.html')


class AdminSettingsAnalyticsModule(tornado.web.UIModule):
    def render(self):
        return self.render_string('admin/uimodules/admin_settings_analytics.html')


class AdminSettingsMapModule(tornado.web.UIModule):
    def render(self):
        return self.render_string('admin/uimodules/admin_settings_map.html')


# #embed map/listing edit js only if we need it
#   def javascript_files(self):
#     js_scripts = ['http://maps.googleapis.com/maps/api/js?\
# key=AIzaSyC563kYWxAveotixreil7UMeKWjDR74lX4&sensor=true',
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
