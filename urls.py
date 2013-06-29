import tornado.web
import db
import forms

from util import MultiValueDict

from pprint import pprint


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    # def get_current_user(self):
    #     user_id = self.get_secure_cookie("user_id")
    #     user = db.get_user(user_id)
    #     if not user: return None
    #     return self.get_secure_cookie("user_id")

    # def somemeth(self): #to pass to css active nav
    #     somevar = self.request.uri
    #     return somevar


class IndexHandler(BaseHandler):
    def get(self):
        self.render('index.html')


class LoginHandler(BaseHandler):
    def get(self):
        form = forms.LoginForm()
        self.render('login.html',form=form)

    # def post(self):
    #     form = forms.RegistrationForm(MultiValueDict(self.request.arguments))
    #     if form.validate():
    #         pprint(MultiValueDict(self.request.arguments))
    #     else:
    #         pprint(form.errors)
    #         print("invalid")
    #         self.render('index.html',form=form)


class AdminHandler(BaseHandler):
    def get(self):
        # pt = self.page_url()
        # pprint(dir(self))
        self.render('admin/admin_index.html')


class AdminSettingsHandler(BaseHandler):
    # form is being pulled in by sMod
    def get(self,settingsModule=None):
        print(settingsModule);
        self.render('admin/admin_settings.html',sMod=settingsModule)


    def post(self,settingsModule=None):
        val = self.get_argument('sitename')
        print(val);
        self.render('admin/admin_settings.html',sMod=settingsModule)



class AdminUsersHandler(BaseHandler):
    def get(self):
        self.render('admin/admin_users.html')


class AdminMessagesHandler(BaseHandler):
    def get(self):
        self.render('admin/admin_messages.html')


handlers = [
    (r"/", IndexHandler),
    (r"/login", LoginHandler),
    (r"/admin", AdminHandler),
    (r"/admin/settings/([^/]+)",AdminSettingsHandler),
    (r"/admin/users", AdminUsersHandler),
    (r"/admin/messages", AdminMessagesHandler),
]
