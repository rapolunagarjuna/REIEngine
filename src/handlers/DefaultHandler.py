from flask import Blueprint, render_template, request, jsonify
from src.services.DefaultService import DefaultService
default = Blueprint("default", __name__)

@default.route("/")
def rerouteToLogin():
    return render_template("rerouteToLogin.html")

@default.route("/signup", methods=['POST'])
def signup():
    data = request.get_json()
    print("Data for signup", data)
    response = DefaultService.signup(data)
    return jsonify(response)

@default.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    print("Data for login", data)
    response = DefaultService.login()
    return jsonify(response)

@default.errorhandler(404)
def pageNotFound():
    return "The requested page does not exists"