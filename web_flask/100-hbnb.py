#!/usr/bin/python3
""" setup flask """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def fitler():
    """ function that lists states """
    states = storage.all(State)
    sort = sorted(states.values(), key=lambda state: state.name)
    amenities = storage.all(Amenity)
    sort1 = sorted(amenities.values(), key=lambda amen: amen.name)
    places = storage.all(Place)
    sort2 = sorted(places.values(), key=lambda plc: plc.name)
    return render_template('100-hbnb.html',
                           states=sort, amenities=sort1, places=sort2)


@app.teardown_appcontext
def teardown_db(exception):
    """ close session after each request """
    return storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
