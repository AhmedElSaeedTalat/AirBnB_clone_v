#!/usr/bin/python3
""" setup flask """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state(id=None):
    """ function that lists states """
    states = storage.all(State)
    if id:
        found_state = ""
        for state in states.values():
            if state.id == id:
                found_state = state
        if found_state:
            return render_template('9-states.html', state=found_state)
        return render_template('9-states.html', error='404')
    sort = sorted(states.values(), key=lambda state: state.name)
    return render_template('9-states.html', states=sort)


@app.teardown_appcontext
def teardown_db(exception):
    """ close session after each request """
    return storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
