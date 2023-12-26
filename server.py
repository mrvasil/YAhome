from flask import Flask, jsonify, render_template, request
import os
from ya_info import *
from send_request import *
import json

devices_with_button = ['devices.types.light', 'devices.types.socket']
devices_with_info = ['devices.types.light', 'devices.types.socket']

with open('secrets.json', 'r', encoding='utf-8') as file:
        token = json.load(file)["token"]


gui_dir = os.path.join(os.path.dirname(__file__), 'interface')

app = Flask(__name__, static_folder=gui_dir, template_folder=gui_dir)


@app.route("/")
def index():
    with open('last_info.json', 'r', encoding='utf-8') as file:
        info = json.load(file)
    
    return render_template('index.html', info=info, devices_with_button=devices_with_button, length=len(info['devices']))


@app.route("/table")
def table():
    global info
    info = info1(devices_with_button, devices_with_info)

    with open('last_info.json', 'w', encoding='utf-8') as file:
        json.dump(info, file)
        
    return render_template('table.html', info=info, devices_with_button=devices_with_button, length=len(info['devices']))



@app.route("/device", methods=["POST"])
def device():
    return send_request(request.form['id'], request.form['state'], token)

@app.route("/get_info")
def get_info():
    return info

app.run(host="0.0.0.0", port=7649)