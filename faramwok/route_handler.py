import typing as ty
from faramwok.doc_parser import DocStringHandler

class RouteHandler:
    def __init__(self, path: str, handler: ty.Callable = None):
        self.path = path
        self.handler = handler
        self.aux_handler = DocStringHandler.from_handler_doc(handler.__doc__)

    def __repr__(self):
        return f"<RouteHandler path={self.path} handler={self.handler}>"

    def handle(self, request):
        if self.aux_handler:
            return self.aux_handler.handle(request)
        elif self.handler:
            return self.handler(request)
        else:
            return None
