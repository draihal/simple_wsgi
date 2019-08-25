# def app(environ, start_response):
#     response_body = b"Hello, World!"
#     status = "200 OK"
#     start_response(status, headers=[])
#     return iter([response_body])

# pip install gunicorn
# gunicorn app:app

from api import API

app = API()


@app.route("/home")
def home(request, response):
    response.text = "Hello from the HOME page."


@app.route("/about")
def about(request, response):
    response.text = "Hello from the ABOUT page."


@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}."


@app.route("/tell/{age:d}")
def greeting(request, response, age):
    response.text = f"Your age are {age}."
