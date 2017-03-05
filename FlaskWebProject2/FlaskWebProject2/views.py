from forms import *
from datetime import datetime
from flask import Flask, render_template, request, url_for,  json, redirect, jsonify
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from FlaskWebProject2 import app
import json

msgs = []


@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods=['POST', 'GET'])
def home():
    fl = False
    data=['1.0', '1.0']
    if len(msgs) > 0:
        fl = True
        json_data=open('data.txt').read()
        data = json.loads(json_data)
    form = Messange()
    if form.validate_on_submit():
        msgs.append([form.msg.data, 'admin'])
        return redirect('/home')
    return render_template('index.html',
        title='Home Page',
        year=datetime.now().year,
        data=msgs,
        form=form,
        fl=fl
       )

@app.route('/postmsg', methods=['POST'])
def postmsg():
    data = request.get_json(force=True)
    messange = data['messange']
    lat = data['location'][0]
    lng = data['location'][1]
    msgs.append([messange, 'user', lat, lng])
    with open('data.txt', 'w') as outfile:
        json.dump([lat, lng], outfile)
    return 'ok'

@app.route('/getmsgs', methods=['GET'])
def getmsg():
    return jsonify(msgs)