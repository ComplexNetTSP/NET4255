from flask import Flask,request
from datetime import datetime
import os
import socket

app = Flask(__name__)
hostname = socket.gethostname()
version = "Roujanski Gatien High Availabilty V2"

@app.route("/")
def main():
    print(request.remote_addr)
    return "<p>"+version+" <br> Server "+hostname+ " "+ str(datetime.now())+"</p>"