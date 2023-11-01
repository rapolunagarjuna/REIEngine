from flask import Blueprint, request, jsonify
from src.services.CalculatorService import CalculatorService

calculator = Blueprint("calculator", __name__, url_prefix="/calculator")


@calculator.route("/", methods=['GET'])
def calculate():
    params = request.args
    print("Params for calculate", params)

    values = CalculatorService.getCalculator(params)
    return jsonify(values)

@calculator.route("/trial", methods=['GET'])
def trial():
    params = request.args
    print("Params for calculate", params)

    values = CalculatorService.getTrial(params)
    return jsonify(values)