#!/usr/bin/python3
""" script to set up flask """
from flask import Flask


app = Flask(__name__)
@app.route('/', strict_slashes=False)
def home():
    """ home(): function to route to home"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
