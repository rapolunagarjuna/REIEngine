from flask import Blueprint, render_template

default = Blueprint("default", __name__)

@default.route("/")
def rerouteToLogin():
    return render_template("rerouteToLogin.html")

@default.errorhandler(404)
def pageNotFound():
    return "The requested page does not exists"