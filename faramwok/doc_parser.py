from faramwok.response import Response
class DocStringHandler:

    KIND = {
        '!html': 'html',
        '!text': 'text',
        '!markdown': 'markdown',
    }

    @classmethod
    def from_handler_doc(cls, handler_doc):

        # Pre-exit if no doc string
        if handler_doc is None:
            return None

        handler_doc_first_line = handler_doc.split('\n')[0]

        # Make sure it follows our doc string pattern.
        if handler_doc_first_line.startswith('!'):
            return cls(handler_doc)

    @staticmethod
    def follows_doc_string(line):
        return line.startswith('!')

    def __init__(self, doc_string):
        self.doc_string = doc_string

    def get_doc_string(self):
        return self.doc_string

    def get_response(self):
        return self.doc_string.split('\n')[1:]

    def handle(self, *args, **kwargs):
        if self.get_type() == 'html':
            return Response(self.get_response(), headers=[('Content-Type', 'text/html')])
        elif self.get_type() == 'text':
            return Response(self.get_response(), headers=[('Content-Type', 'text/plain')])

    def get_type(self):
        kind = self.doc_string.split('\n')[0].strip()
        if kind in self.KIND:
            return self.KIND[kind]
