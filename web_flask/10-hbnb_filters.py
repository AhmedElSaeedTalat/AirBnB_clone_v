#!/usr/bin/python3
""" setup flask """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def fitler(id=None):
    """ function that lists states """
    states = storage.all(State)
    sort = sorted(states.values(), key=lambda state: state.name)
    amenities = storage.all(Amenity)
    sort1 = sorted(amenities.values(), key=lambda amen: amen.name)
    return render_template('10-hbnb_filters.html',
                           states=sort, amenities=sort1)


@app.teardown_appcontext
def teardown_db(exception):
    """ close session after each request """
    return storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
