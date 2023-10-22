#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
""" setup flask """


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """ function that lists states """
    states = storage.all(State)
    dict_state = {}
    for key, state in states.items():
        dict_state[state.id] = state.name
    return render_template('7-states_list.html', states=dict_state)


@app.teardown_appcontext
def after_request(error=None):
    """ close session after each request """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
