from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap

import folium
from folium.plugins import FastMarkerCluster
from folium.plugins import Fullscreen
from folium import FeatureGroup, LayerControl, Map, Marker
import datetime
import flask_excel as excel

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

@app.route('/maps')
def maps():
    return render_template('maps.html')   

@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        return jsonify({"result": request.get_array(field_name='file')})
    return '''
    <!doctype html>
    <title>Upload an excel file</title>
    <h1>Excel file upload (csv, tsv, csvz, tsvz only)</h1>
    <form action="" method=post enctype=multipart/form-data><p>
    <input type=file name=file><input type=submit value=Upload>
    </form>
    '''


@app.route("/download", methods=['GET'])
def download_file():
    return excel.make_response_from_array([[1, 2], [3, 4]], "csv")


@app.route("/export", methods=['GET'])
def export_records():
    return excel.make_response_from_array([[1, 2], [3, 4]], "csv",
                                          file_name="export_data")    


if __name__ == '__main__':
    app.run(port=5000,debug=True)    