#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

 # Generate a UUID
    cache_id = uuid.uuid4()
    
    css_links = [
    '/static/styles/4-common.css',
    '/static/styles/3-header.css',
    '/static/styles/3-footer.css',
    '/static/styles/6-filters.css',
    '/static/styles/8-places.css'
]

    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           css_links=css_links,
                           cache_id=cache_id) 

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
