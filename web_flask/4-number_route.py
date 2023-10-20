#!/usr/bin/python3
""" script to set up flask """
from flask import Flask, abort
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ home(): function to route to home"""
    return "Hello HBNB!"


@app.route('/hbnb',  strict_slashes=False)
def hbnb():
    """ hbnb(): return new route """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    """ show_text(): show key word in url """
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def py_url(text=None):
    """ py_url(text): add URL with python and keyword
    example:
    /python/<keyword>
    Args:
        text: keyword passed to use
    """
    if text:
        text = text.replace("_", " ")
        return f"Python {escape(text)}"
    else:
        return "Python is cool"


@app.route('/number/<n>', strict_slashes=False)
def num(n):
    """ num(n): passing route with number
    Args:
       n: number passed
    """
    try:
        int(n)
        return f"{n} is a number"
    except ValueError:
        return abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
