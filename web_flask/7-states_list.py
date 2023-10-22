#!/usr/bin/python3
""" setup flask """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """ function that lists states """
    states = storage.all(State)
    sort = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=sort)


@app.teardown_appcontext
def after_request(exception):
    """ close session after each request """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
