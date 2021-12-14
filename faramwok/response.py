class Response:
    def __init__(self, body, status='200 OK', headers=None):
        if headers is None:
            headers = [('Content-Type', 'text/html;charset=utf-8')]
        self.headers = headers
        self.body = body
        self.status = status

    def __iter__(self):
        yield self.body.encode('utf8')
