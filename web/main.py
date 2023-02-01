from flask import Flask,request
from datetime import datetime
from pymongo import MongoClient
import os
import socket

app = Flask(__name__)
print(f"### Connect to mongodb uri: { os.environ.get('MONGO_URL') }")
client=MongoClient(os.environ.get("MONGO_URL"))
hostname = socket.gethostname()
version = "Roujanski Gatien High Availabilty V2"

@app.route("/")
def main():
    print(request.remote_addr)
    db = client.logs
    collection=db['flask']
    collection.insert_one({"ip": request.remote_addr, "date": str(datetime.now()),"server":hostname})
    return "<p>"+version+" <br> Server "+hostname+"<br> See /logs </p>"

@app.route("/logs")
def logs():
    print(request.remote_addr)
    db = client.logs
    collection=db['flask']

    cursor = collection.find({})
    res="<p>"+version+"<br> Server "+hostname+"<br>"
    for doc in cursor:
        res=res+str(doc["ip"])+" "+str(doc['date'])+" "+str(doc["server"])+"<br>"
    res=res+"</p>"
    return res