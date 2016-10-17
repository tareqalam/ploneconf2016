from wsgiref.simple_server import make_server
import sys
import re
import traceback
from cgi import escape


class Request(object):

    def __init__(self, environ):
        self.environ = environ
        self.path = environ["PATH_INFO"]
        self.method = environ['REQUEST_METHOD']
        self.environ['SERVER_PROTOCOL'] = 'HTTP'
        self.headers = {k: v for k, v in environ.items() if k.startswith("HTTP_")}
        self.params = None
        self.GET = environ["QUERY_STRING"]
        self.POST = {}


class Response(object):

    def __init__(self, status="200 OK", body=""):
        self.status = status
        self.body = str(body)
        self.headers = {
            "Content-Type": "text/html",
            "Content-Length": str(len(self.body))
        }

    @property
    def wsgi_headers(self):
        return [(k, v) for k, v in self.headers.items()]


class MicroFramework(object):

    def __init__(self):
        self.routes = {}

    def __call__(self, environ, start_response):
        response = self.dispatch(Request(environ))
        start_response(response.status, response.wsgi_headers)
        return "{0}\n".format(response.body)

    @staticmethod
    def not_found():
        return Response(
            status="404 Not Found",
            body="Page not found."
        )

    @staticmethod
    def internal_error():
        return Response(
            status="500 Internal Server Error",
            body="An error has occurred."
        )

    def route(self, route_regex):
        def route_decorator(fn):
            self.routes[route_regex] = fn
            return fn

        return route_decorator

    def dispatch(self, request):
        for regex, view_func in self.routes.items():
            match = re.search(regex, request.path)
            if match is not None:
                # import pdb;pdb.set_trace()
                request.params = match.groups()

                try:
                    return view_func(request)
                except Exception:
                    
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    traceback.print_tb(exc_traceback)
                    return self.internal_error()

        return self.not_found()




# httpd = make_server('', 8000, hello_world_app)
print("Serving on port 8000")

# Serve until process is killed
# httpd.serve_forever()


# def log_environ(handler):
#    """
#    print the environment dictionary to the consile
#    """
#    from pprint import pprint

#    def _inner(environ, start_function):
#        pprint(environ)
#        return handler(environ, start_function)
#    return _inner

# this will show hello world in your browser

# app = log_environ(hello_world_app)

app = MicroFramework()


@app.route("^/logout/?$")
def logout(request):
  return Response(body="Bye bye")


@app.route("^/helloworld/?$")
def hello_world(request):
    # status = '200 OK'  # HTTP Status
    # HTTP Headers
    # headers = [('Content-type', 'text/plain; charset=utf-8')]
    # start_repspone(status, headers)
    # The returned object is going to be printed
    import pdb;pdb.set_trace()
    return Response(body="hello world")

httpd = make_server("localhost", 8000, app)
httpd.serve_forever()
