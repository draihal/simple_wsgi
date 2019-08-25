from api import API

app = API()


def index_page(req, resp):
    resp.text = "Hello from the INDEX page."


def home_page(req, resp):
    resp.text = "Hello from the HOME page."


app.add_route("/", index_page)
app.add_route("/home", home_page)
app.add_route("/home/", home_page)


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
@app.route("/template/")
def template_handler(req, resp):
    resp.body = app.template(
        "index.html",
        context={"title": "WSGI Framework", "body": "Testing template with jinja."}
    ).encode()


def custom_exception_handler(request, response, exception_cls):
    response.text = "Oops! Something went wrong."


app.add_exception_handler(custom_exception_handler)


@app.route("/except")
@app.route("/except/")
def exception_throwing_handler(request, response):
    raise AssertionError("Testing exeption.")
