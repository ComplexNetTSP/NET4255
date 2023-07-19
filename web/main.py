from flask import Flask,request
from datetime import datetime
from pymongo import MongoClient
import os
import socket

app = Flask(__name__)
app.config["MONGO_URL"]="mongodb://mongo:27017/dev"
mongo=PyMongo(app)
db=mongo.db
hostname = socket.gethostname()
version = "Roujanski Gatien High Availabilty V2"

@app.route("/")
def main():
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

@app.route("/db")
def main():
    print(request.remote_addr)
    collection=db['flask']
    collection.insert_one({"ip": request.remote_addr, "date": str(datetime.now()),"server":hostname})
    return "<p>"+version+" <br> Server "+hostname+"<br> See /logs </p>"
