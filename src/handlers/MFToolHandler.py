from flask import Blueprint, request, jsonify
from src.services.MFToolService import MFToolService

mftool = Blueprint("mftool", __name__, url_prefix="/mftool")


@mftool.route("/check-rates", methods=['GET'])
def checkRates():
    params = request.args
    print("Params for checkRates", params)

    rates = MFToolService.checkRates(params)
    return jsonify(rates)


@mftool.route("/calculate", methods=['GET'])
def calculate():
    params = request.args
    print("Params for calculate", params)

    values = MFToolService.calculate(params)
    return jsonify(values)

@mftool.route("/calculate-affordability", methods=['GET'])
def calculateAffordability():
    params = request.args
    print("Params for calculateAffordability", params)

    affordability = MFToolService.calculateAffordability(params)
    return jsonify(affordability)

@mftool.route("/check-equity-rates", methods=['GET'])
def checkEquityRates():
    params = request.args
    print("Params for checkEquityRates", params)

    rates = MFToolService.checkEquityRates(params)
    return jsonify(rates)

@mftool.route("/finance/rates", methods=['GET'])
def financeRates():
    params = request.args
    print("Params for financeRates", params)

    rates = MFToolService.financeRates(params)
    return jsonify(rates)