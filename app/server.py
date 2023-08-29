"""
Flask REST API for test-task
"""

import socket
import os
import waitress
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)


@app.route("/id", methods=["GET"])
@cross_origin()
def getid():
    return jsonify({"id": os.getenv("UUID")})


@app.route("/author", methods=["GET"])
@cross_origin()
def getauthor():
    return jsonify({"author": os.getenv("AUTHOR")})


@app.route("/hostname", methods=["GET"])
@cross_origin()
def gethostname():
    return jsonify({"hostname": socket.gethostname()})


if __name__ == "__main__":
    waitress.serve(app, host="0.0.0.0", port=8000)
