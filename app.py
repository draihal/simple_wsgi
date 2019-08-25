# def app(environ, start_response):
#     response_body = b"Hello, World!"
#     status = "200 OK"
#     start_response(status, headers=[])
#     return iter([response_body])

# pip install gunicorn
# gunicorn app:app

from api import API

app = API()


# @app.route("/home")
# def home(request, response):
#     response.text = "Hello from the HOME page."
#
#
# @app.route("/about")
# def about(request, response):
#     response.text = "Hello from the ABOUT page."

def handler(req, resp):
    resp.text = "Hello from the HOME page."


def handler2(req, resp):
    resp.text = "Hello from the INDEX page."


app.add_route("/home", handler)
app.add_route("/", handler2)


@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}."


@app.route("/age/{age:d}")
def greeting(request, response, age):
    response.text = f"Your age are {age}."


@app.route("/test")
@app.route("/test/")
class TestResource:
    def get(self, req, resp):
        resp.text = "Test Page"

@app.route("/template")
def template_handler(req, resp):
    resp.body = app.template(
        "index.html",
        context={"title": "WSGI Framework", "body": "Testing template with jinja."}
    ).encode()

