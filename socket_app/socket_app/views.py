from socket_app import app, socketio
from flask import Flask, render_template, request, url_for,  json, redirect, jsonify
from flask_socketio import send
import json
msgs=[]


@socketio.on( 'admin_msg' )
def admin_msg( jsonm ):
  msgs.append([jsonm['message'], 'admin'])
  socketio.emit( 'admin_msg_add', jsonm)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@app.route('/postmsg', methods=['POST'])
def postmsg():
    data = request.get_json(force=True)
    message = data['messange']
    lat = data['location'][0]
    lng = data['location'][1]
    msgs.append([message, 'user', lat, lng])
    inf={'message': message, 'lat': lat, 'lng': lng}
    socketio.emit( 'user_msg_add', inf)
    return 'ok'

@app.route('/adduser', methods=['POST'])
def adduser():
    data = request.get_json(force=True)
    user_id = data['id']
    socketio.emit( 'adduser',user_id)
    return 'ok'

@app.route('/getmsgs', methods=['GET'])
def getmsg():
    return jsonify(msgs)