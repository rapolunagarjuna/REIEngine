from flask import Blueprint, render_template, request, jsonify
from src.services.PropertyService import PropertyService

property = Blueprint("property", __name__, url_prefix="/property")


@property.route("/details", methods=['GET'])
def getPropertyDetails():
    params = request.args
    print("Params for getPropertyDetails",params)

    details = PropertyService.getPropertyDetails(params)
    return jsonify(details)

@property.route("/list", methods=['GET'])
def getPropertyList():
    params = request.args
    print("Params for getPropertyList", params)
    
    propertyList =  PropertyService.getPropertyList(params)
    return jsonify(propertyList)

@property.route("/similar", methods=['GET'])
def getSimilarPropertyList():
    params = request.args
    print("Params for getSimilarPropertyList", params)
    
    similarProperties =  PropertyService.getSimilarPropertyList(params)
    return jsonify(similarProperties)

@property.route("/photos", methods=['GET'])
def getPropertyPhotos():
    params = request.args
    print("Params for getPropertyPhotos", params)
    
    photos =  PropertyService.getPropertyPhotos(params)
    return jsonify(photos)

@property.route("/commute-time", methods=['GET'])
def getCommuteTime():
    params = request.args
    print("Params for getCommuteTime", params)
    
    commuteTime =  PropertyService.getCommuteTime(params)
    return jsonify(commuteTime)

@property.route("/surroundings", methods=['GET'])
def getSurroundings():
    params = request.args
    print("Params for getSurroundings", params)
    
    surroundings =  PropertyService.getSurroundings(params)
    return jsonify(surroundings)