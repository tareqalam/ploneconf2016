
import sys
import re
import traceback


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
                request.params = match.groups()

                try:
                    return view_func(request)
                except Exception:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    traceback.print_tb(exc_traceback)
                    return self.internal_error()

        return self.not_found()
