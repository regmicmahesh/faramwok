
import re
import typing as ty
from faramwok.request import Request
from faramwok.response import Response
from faramwok.route_handler import RouteHandler
from wsgiref.handlers import SimpleHandler

HANDLER_TYPE = ty.Callable[..., Response]


class Application:
    def __init__(self):
        self.routes: list[RouteHandler] = []

    def add(self, path, handler):
        route_handler = RouteHandler(path, handler)
        self.routes.append(route_handler)

    def match(self, path):
        for route in self.routes:
            m = re.match(route.path, path)
            if m:
                return route
        return None

    def route(self, path):
        def decorator(handler: ty.Callable[..., Response]):
            self.add(path, handler)
            return handler
        return decorator

    def __call__(self, environ, start_response):
        route = self.match(environ['PATH_INFO'])
        if route:
            request = Request(environ)
            response = route.handler(request)
            start_response(response.status, response.headers)
            return response(environ, start_response)
        else:
            start_response('404 Not Found', headers=[
                           ('Content-Type', 'text/plain')])
            return [b'Not Found']
