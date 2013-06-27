#settings
import os.path
import uimodules


from tornado.options import define

define("port",   default=8888,  help="run on given port",type=int)
define("config", default=None,  help="tornado config file")
define("debug",  default=False, help="debug mode")


settings = dict(
    template_path = os.path.join(os.path.dirname(__file__),'templates'),
    static_path   = os.path.join(os.path.dirname(__file__),'static'),
    upload_path   = os.path.join(os.path.dirname(__file__),'static/upload'),
    xsrf_cookies  =True,
    cookie_secret ="11oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2Xdwe1o%Vo",
    login_url     ="/login",
    autoescape    =None,
    ui_modules    =uimodules,
    debug         = True
)


