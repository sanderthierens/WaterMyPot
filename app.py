import sys
from flask import Flask
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import get_jwt
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from input_pump_module import *


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "superdupersecret"  # Change this!
jwt = JWTManager(app)

@app.route("/login")
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    access_token = create_access_token(identity="sander")
    return access_token
    # return jsonify(access_token=access_token)

@app.route('/protected', methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route("/pumpy")
def pumpy():
    pump(5, 11)
    return "hello, World pump"

@app.route("/pump")
@jwt_required()
def hello_world():
    claims = get_jwt()
    print(claims["sub"])
    duration = int(claims["sub"])
    pump(duration, 11)
    return "hello, World pump"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
