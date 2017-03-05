"""
The flask application package.
"""

from flask import Flask
from flask_googlemaps import GoogleMaps

app = Flask(__name__)
app.secret_key='you should not pass'
GoogleMaps(app, key="AIzaSyCqjPaHR2s1Nid837TNgRLxFgWY7qB0jeo")
import FlaskWebProject2.views
