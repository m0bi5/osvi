#!/usr/bin/env python
import paho.mqtt.client as mqtt
import ssl,time,json
import base64
username='alumcardosvi'
password='MDKVgVw=xh6A#=2N'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, message):
    data=str(message.payload.decode("utf-8"))
    requestId=json.loads(data)
    print("Response received for ",requestId['requestId'])
    with open('../docker_flask/'+requestId['requestId'],'w') as f:
        f.write(data)

def on_publish(client, userdata, message):
    print("Message Published = ",message)

def on_subscribe(client,userdata,mid,granted_qos):
    print("Subscribed")

client = mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message
client.on_subscribe=on_subscribe
client.username_pw_set(username,password)
client.tls_set(ca_certs='iris.crt', certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,tls_version=ssl.PROTOCOL_TLS, ciphers=None)
client.tls_insecure_set(True)
client.connect("mqtt.iris.nitk.ac.in", 8883, 60)
print("Subscribing to topic","alumcardosvi")   
client.subscribe("alumcardosvi/res")
client.loop_forever()
