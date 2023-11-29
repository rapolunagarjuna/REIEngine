from flask import Blueprint, request, jsonify
from src.services.UserService import UserService

user = Blueprint("user", __name__, url_prefix="/user")

@user.route("/", methods=['GET'])
def getAllUsers():
    users = UserService.getAllUsers()
    return jsonify(users)

@user.route("/", methods=['POST'])
def addNewUser():
    user_data = request.get_json()  # Assuming you're sending JSON data in the request

    # Call the service method to add a new user
    responseJSON = UserService.addNewUser(user_data)

    return jsonify(responseJSON), responseJSON["status_code"]

    