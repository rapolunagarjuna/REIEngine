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

@calculator.route("/", methods=['POST'])
def setCalculator():
    params = request.args
    data = request.get_json()
    print("Data for setCalculator", data)

    # Convert all values to strings
    for key in data:
        for k, v in data[key].items():
            data[key][k] = str(v)

    # Define keys and their corresponding default values as strings
    defaults = {
        "propertyInfo": {
            "vacancyRate": 5,
            "managementRate": 5,
            "advertizingCost": 100,
            "annualAppreciationRate": 3,
        },
        "purchaseInfo": {
            "repairs": 5000,
            "repairsContingency": 1000,
            "lenderFee": 1500,
            "brokerFee": 5000,
            "environmentals":0,
            "inspections": 700,
            "appraisals": 700,
            "misc": 500,
            "transferTax": 0,
            "legal": 500,
        },
        "incomeInfo": {
            "grossRents": 58800,
            "parking": 0,
            "storage": 0,
            "laundry": 0,
            "other": 0,
        },
        "financing": {
            "firstMtgPrincipleAmount": 355300,
            "firstMtgInterestRate": 8,
            "firstMtgAmortizationPeriod": 30,
            "firstMtgCMHCFee": 0,
            "secondMtgPrincipleAmount": 0,
            "secondMtgInterestRate": 12,
            "secondMtgAmortizationPeriod": 9999,
        },
        "operating": {
            "repairsRate": 2940,
            "electricity":0,
            "gas": 0,
            "lawn": 0,
            "water": 1200,
            "cable": 1200,
            "caretaking": 2880,
            "associationFees": 0,
            "trashRemoval": 0,
            "miscellaneous": 0,
            "commonAreaMaintenance": 0,
            "capitalImprovements":0,
            "accounting": 0,
            "legal": 0,
            "badDebts": 0,
            "other": 0,
        }
    }

    for key, default_value in defaults.items():
        if key not in data:
            data[key] = default_value
        else:
            # Check if all values for this key are positive integers or floats
            for k, v in data[key].items():
                if not (v.replace(".", "", 1).isdigit() and float(v) >= 0):
                    return jsonify({"error": f"'{k}' should be a positive float or integer."})
                data[key][k] = float(v) if "." in v else int(v)  # Convert to int if it's an integer

            # Further check for specific keys in specific ranges
            if key in ["propertyInfo", "financing", "operating"]:
                for k, v in data[key].items():
                    if k in [
                        "vacancyRate", "managementRate", "annualAppreciationRate",
                        "firstMtgInterestRate", "secondMtgInterestRate", "repairsRate"
                    ]:
                        if not (0 <= float(v) <= 100):
                            return jsonify({"error": f"'{k}' should be a float or integer between 0 and 100."})

    # Further actions with the data, for instance, passing this data to a service
    # Assuming you have a CalculatorService method to set calculator values
    values = CalculatorService.setCalculator(params, data)

    return jsonify(values)


