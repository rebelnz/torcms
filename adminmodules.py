import tornado.web
import forms
import db
from time import strftime


class AdminSideNavModule(tornado.web.UIModule):
    def render(self):
        return self.render_string('admin/admin_side_nav.html')


class AdminTopNavModule(tornado.web.UIModule):
    def render(self):
        # to set active class + we can add new items to nav
        nav_items = (
            ("/admin","Admin","icon-lock"),
            ("/admin/settings/site","Settings","icon-cog"), # /site url default
            ("/admin/users","Users","icon-user"),
            ("/admin/messages","Messages","icon-inbox"),
            ("/","View Site","icon-eye-open")
            )
        return self.render_string('admin/admin_top_nav.html',
                                  nitems = nav_items)

    
class AdminSettingsNavModule(tornado.web.UIModule):
    def render(self):
        nav_items = (
            ("/admin/settings/site","Site"),
            ("/admin/settings/map","Map"),
            ("/admin/settings/social","Social"),
            ("/admin/settings/home","Home Page"),
            ("/admin/settings/analytics","Analytics"),
            ("/admin/settings/data","Data"),
            ("/admin/settings/campaign","Campaign"),
            ("/admin/settings/calendar","Calendar"),
            )

        return self.render_string('admin/uimodules/admin_settings_nav.html',
                                  nitems = nav_items)

    # def css_files(self):
    #     return "/static/css/admin-settings-site.css"

    # settings module
class AdminSettingsSiteModule(tornado.web.UIModule):
    def render(self):
        data = db.get_site_settings()
        if data:
            settings = data
            settings["updated"] = data["updated"].ctime() #format time
        else:
            settings = False
        return self.render_string('admin/uimodules/admin_settings_site.html',
                                  settings=settings,
                                  )
    #settings form
class AdminSettingsSiteFormModule(tornado.web.UIModule):
    def render(self):
        data = db.get_site_settings()
        if data: #repopulate form
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

    # map module
class AdminSettingsMapModule(tornado.web.UIModule):
    def render(self):
        form = forms.AdminSettingsAddressForm() # from forms file
        return self.render_string('admin/uimodules/admin_settings_map.html')

    def css_files(self):
        return ['/static/css/admin-settings-map.css',
                'http://cdn.leafletjs.com/leaflet-0.5/leaflet.css']

    def javascript_files(self):
        return ['http://cdn.leafletjs.com/leaflet-0.5/leaflet.js',
        '/static/js/admin-map.js','/static/js/config.js']


    # address module    
class AdminSettingsAddressFormModule(tornado.web.UIModule):
    def render(self):
        data = db.get_address_settings()
        if data: #repopulate form
            form = forms.AdminSettingsAddressForm(
                address=data["address"],
                suburb=data["suburb"],
                city=data["city"],
                zipcode=data["zipcode"]
                )
        else:
          form = forms.AdminSettingsAddressForm() # from forms file
        return self.render_string('admin/forms/admin_settings_address_form.html',
                                  form=form,
                                  )

    # social module
class AdminSettingsSocialModule(tornado.web.UIModule):
    def render(self):
        data = db.get_social_settings()
        if data:
            settings = data
            settings["updated"] = data["updated"].ctime() #format time
        else:
            settings = False
        return self.render_string('admin/uimodules/admin_settings_social.html',
                                  settings=settings,
                                  )
    # form
class AdminSettingsSocialFormModule(tornado.web.UIModule):
    def render(self):
        data = db.get_social_settings()
        if data: #repopulate form
            form = forms.AdminSettingsSocialForm(
                facebook=data["facebook"],
                googleplus=data["googleplus"],
                kakao=data["kakao"],
                twitter=data["twitter"],
                linkedin=data["linkedin"]
                )
        else:
            form = forms.AdminSettingsSocialForm() # from forms file
        return self.render_string('admin/forms/admin_settings_social_form.html',
                                  form=form,
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

    def javascript_files(self):
        return ['/static/js/tracker.js']


class AdminPagesFormModule(tornado.web.UIModule):
    def render(self):
        form = forms.AdminPagesForm() # from forms file
        return self.render_string('admin/forms/admin_pages_add_form.html', form=form)


