# simple wsgi

## Description
> This is a Python Web Framework built for learning. 
It is a WSGI framework and can be used with any WSGI application server such as Gunicorn.
```
pip install gunicorn
```
And then start the server:
```
gunicorn app:app (for example)
```

## Installation

clone the repo:
```
git clone https://github.com/draihal/simple_wsgi
cd simple_wsgi
```
create virtual environment and install package in it:
```
python -m venv venv
source venv/bin/activate or venv\Scripts\activate (on Win)
python setup.py install
```
or install package global:
```
python setup.py install
```
to uninstall:
```
pip uninstall simple_wsgi
```

## Usage example
```python
from api import API

app = API()


# Simple routing like in Flask
@app.route("/")
def index_page(request, response):
    response.text = "Hello from the INDEX page."


# Simple routing like in Django
def home_page(request, response):
    response.text = "Hello from the HOME page."


app.add_route("/home", home_page)
app.add_route("/home/", home_page)


# Class Based Handlers with your methods (there only get)
@app.route("/test")
@app.route("/test/")
class TestResource:
    def get(self, request, response):
        response.text = "Test Page"


# Parameterized routing
@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}."


# Parameterized routing
@app.route("/age/{age:d}")
def greeting(request, response, age):
    response.text = f"Your age are {age}."


# Support for templates with jinja templating language
@app.route("/template")
@app.route("/template/")
def template_handler(request, response):
    response.body = app.template(
        "index.html",
        context={"title": "WSGI Framework", "body": "Testing template with jinja."}
    ).encode()


# Custom exception handler
def custom_exception_handler(request, response, exception_cls):
    response.text = "Oops! Something went wrong."


app.add_exception_handler(custom_exception_handler)


@app.route("/except")
@app.route("/except/")
def exception_throwing_handler(request, response):
    raise AssertionError("Testing exeption.")

```