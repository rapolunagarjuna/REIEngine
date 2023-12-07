from flask import Blueprint, request, jsonify
from src.services.PropertyService import PropertyService
from src.services.PropertyRentEstimateService import PropertyRentEstimateService
from src.services.CalculatorService import CalculatorService
import concurrent.futures
import threading
import time 


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

@property.route("/list/v-2", methods=['GET'])
def getListingWithCalulator():
    params = request.args
    print("Params for getListingWithCalulator", params)

    propertyList =  PropertyService.getPropertyList(params)
    propertyData = propertyList['data']['home_search']['results'][0]
    address = propertyData['location']["address"]['city'] + ", " +  propertyData['location']["address"]['country']+ ", " +  propertyData['location']["address"]['postal_code']
    api_call_rent_estimate = PropertyRentEstimateService.getPropertyRentEstimateGeneral(address)

    if (api_call_rent_estimate["status_code"] != 200):
        return jsonify({"error": "Rent Estimate API" + api_call_rent_estimate['message']}), api_call_rent_estimate['status_code']

    annualRent = api_call_rent_estimate['rent']  * 12

    from_value = int(params.get("from", 0))
    to_value = int(params.get("to", 10))

    if (from_value < 0 or from_value >= to_value or to_value >= len(propertyList['data']['home_search']['results'])):
        return jsonify({"error": "wrong argument values for from and to"}), 401

    results = []
    threads = []

    def process_property(i):
        property_id = propertyList['data']['home_search']['results'][i]['property_id']
        param_for_calculator = {"property_id": property_id}
        data = CalculatorService.get_Calculator_temporary(param_for_calculator, annualRent)

        result = propertyList['data']['home_search']['results'][i].copy()
        result["data"] = data
        results.append(result)

    # Create a ThreadPoolExecutor with a maximum of 5 threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(from_value, to_value):
            thread = executor.submit(process_property, i)
            threads.append(thread)
            time.sleep(1)  # Sleep for 1 second to control the rate

    # Wait for all threads to complete
    concurrent.futures.wait(threads)

    propertyList['data']['home_search']['count'] = len(results)
    propertyList['data']['home_search']['results'] = results

    return jsonify(propertyList)
