#!/usr/bin/env python
from flask import Flask,session,render_template,redirect,request
#import mqtt
import sys
import json
import os
import random
import string

app = Flask(__name__)
app.secret_key = 'ansdahjrehrwSXajswdeBEJFkadn'

@app.route('/',methods=['POST','GET'])
def home():
    if request.method=='POST':
        requestId=''.join(random.choices(string.ascii_letters + string.digits, k=16))
        session['requestId']=requestId
        sendToIris=json.dumps({'requestId':requestId,'cardId':request.form['uid']})
        #mqtt.client.publish("alumcardosvi/req",sendToIris)
        return redirect('/loading')
      
    return render_template("home.html")

@app.route('/loading',methods=['POST','GET'])
def loading():
    return render_template("loading.html")

@app.route('/checkForResponse',methods=['GET'])
def checkForResponse():
    requestId=session['requestId']
    os.chdir('../shared')
    exists=os.path.exists(requestId)
    os.chdir('../server')
    if exists:
        return json.dumps(True)
    else:
        return json.dumps(False)

@app.route('/details',methods=['GET'])
def details():
    requestId=session['requestId']
    os.chdir('../shared')
    with open(requestId,'r') as f:
        irisResponse=f.read()
    os.chdir('../server')
    data,image=irisResponse.split('IMAGE_RETURNED')
    context=json.loads(data)
    context['image']=image
    os.chdir('../shared')
    os.remove(requestId)
    os.chdir('../server')
    session.pop('requestId',None)
    return render_template("details.html",context=context)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
