#!/usr/bin/python3
# script to set up flask
from flask import Flask
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
