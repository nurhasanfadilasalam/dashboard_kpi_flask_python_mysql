from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

import folium
from folium.plugins import FastMarkerCluster
from folium.plugins import Fullscreen
from folium import FeatureGroup, LayerControl, Map, Marker
import datetime

import numpy as np
import pandas as pd
# import geopandas
from shapely.geometry import Point

import requests
import json
import re
import urllib.request

app = Flask(__name__)
Bootstrap(app)


@app.context_processor
def inject_today_date():
    return {'year': datetime.date.today().year}

    
@app.route("/dashboard")
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')    


if __name__ == '__main__':
    app.run(port=5000,debug=True)    