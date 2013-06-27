import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.autoreload

from tornado.options import options

from settings import settings
from urls import handlers

class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self,handlers,**settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
