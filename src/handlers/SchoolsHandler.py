from flask import Blueprint, request, jsonify
from src.services.SchoolsService import SchoolsService

schools = Blueprint("schools", __name__, url_prefix="/schools")


@schools.route("/list", methods=['GET'])
def getSchoolsList():
    params = request.args
    print("Params for getSchoolsList", params)

    rates = SchoolsService.getSchoolsList(params)
    return jsonify(rates)

@schools.route("/detail", methods=['GET'])
def getSchoolsDetail():
    params = request.args
    print("Params for getSchoolsDetail", params)

    rates = SchoolsService.getSchoolsDetail(params)
    return jsonify(rates)

@schools.route("/district", methods=['GET'])
def getSchoolsDistrict():
    params = request.args
    print("Params for getSchoolsDistrict", params)

    rates = SchoolsService.getSchoolsDistrict(params)
    return jsonify(rates)


