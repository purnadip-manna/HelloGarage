from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from numberplate import getCarNumber
from makeqr import gen_qr
import requests
import os


app = Flask(__name__)

GARAGE_ID = "1" #os.environ["GARAGE_ID"]
HOST_URL = "http://127.0.0.1:8000"
NEW_VCREATE = "/gapp/newvehicle"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entry')
def enrty():
    return render_template('entry.html')

@app.route('/exit')
def exitp():
    return render_template('exit.html')

@app.route('/uploader1', methods=['POST'])
def uploader1_file():
    if request.method == 'POST':
        f = request.files['file']
        fileName = secure_filename(f.filename)
        f.save(fileName)
        res = getCarNumber(fileName)
        res = res.replace(" ", "")
        data = {
            "garage_id" : int(GARAGE_ID),
            "carno" : res
        }
        requests.post(HOST_URL+NEW_VCREATE, json=data)
        endpoint = HOST_URL+"/gapp/update/"+res+"/"+GARAGE_ID
        gen_qr(endpoint, "entry.png")
        return render_template('showQR1.html')

@app.route('/uploader2', methods=['POST'])
def uploader2_file():
    if request.method == 'POST':
        f = request.files['file']
        fileName = secure_filename(f.filename)
        f.save(fileName)
        res = getCarNumber(fileName)
        res = res.replace(" ", "")
        endpoint = HOST_URL+"/gapp/exitverify/"+res+"/"+GARAGE_ID
        gen_qr(endpoint, "exit.png")
        return render_template('showQR2.html')


if __name__ == '__main__':
    app.run(debug=True)
