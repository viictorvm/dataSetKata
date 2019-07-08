from tornado.web import RequestHandler


class CustomRequestHandler(RequestHandler):
    AUTHORIZATION_HEADER = 'Authorization'

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header('Access-Control-Allow-Methods', 'POST')

    def options(self):
        self.set_status(204)
        self.finish()

    def data_received(self, chunk):
        pass
