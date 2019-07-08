
import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line
from settings import API_PORT
from src.handlers.single_filter_data_handler import SingleFilterDataHandler

define("port", default=API_PORT, help="run on the given port", type=int)


class ApplicationTornado(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/dataset', SingleFilterDataHandler,),
        ]
        tornado.web.Application.__init__(self, handlers)


if __name__ == '__main__':
    app = ApplicationTornado()
    parse_command_line()
    app.listen(options.port)
    tornado.autoreload.start()
    tornado.ioloop.IOLoop.instance().start()
