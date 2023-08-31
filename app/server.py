"""
Flask REST API for test-task
"""

import socket
import os
import waitress
from datetime import datetime
from flask import Flask, jsonify, Response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)


def template(val: str, desc: str):
    return {"value": val, "description": desc, "timestamp": datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')}


@app.route("/", methods=["GET"])
@cross_origin()
def getRoot():
    return Response(status=200)

@app.route("/id", methods=["GET"])
@cross_origin()
def getid():
    return jsonify(template(os.getenv("UUID"),"Pod uuid"))


@app.route("/author", methods=["GET"])
@cross_origin()
def getauthor():
    return jsonify(template(os.getenv("AUTHOR"),"Author's name"))


@app.route("/hostname", methods=["GET"])
@cross_origin()
def gethostname():
    return jsonify(template(socket.gethostname(),"Hostname"))


if __name__ == "__main__":
    waitress.serve(app, host="0.0.0.0", port=8000)
