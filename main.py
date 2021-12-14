from faramwok import Application, Request, Response


app = Application()


@app.route("/")
def index(request: Request):
    """
    <h3>Hi how are you?</h3>
    """
    
    return Response("hello world")
