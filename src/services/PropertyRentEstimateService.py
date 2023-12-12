
import requests

# Store it via KMS in future
APIKEY = '15b63793c0msh3b2f4de33a71f63p1477eejsncdb493315488'
HOST = "realtymole-rental-estimate-v1.p.rapidapi.com"

HEADERS = {
    "X-RapidAPI-Key": APIKEY,
    "X-RapidAPI-Host": HOST
}


URL = "https://realtymole-rental-estimate-v1.p.rapidapi.com/rentalPrice"


class PropertyRentEstimateService:

    @staticmethod
    def getPropertyRentEstimate(address, propertyType, bedrooms, bathrooms, squareFootage, compCount):
        #   address is required parameter, the format is Street, City, State, Zip
        #   propertyType is optional parameter, example include Single Family
        #   bedrooms is optional parameter, example include 5
        #   bathrooms is optional parameter, example include 4
        #   squareFootage is optional parameter, example include 1600
        #   compCount is optional parameter, it is used to compare compCount number of properties, defaults to 10 if not specified. usually between 5-25
        #   property radius here is 50

        querystring = {
            "address": address,
            "propertyType": propertyType,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "squareFootage": squareFootage,
            "compCount": compCount
        }

        response = requests.get(URL, headers=HEADERS, params=querystring)
        print(response)

        if response.status_code != 200:
            print("getPropertyRentEstimate response: ", response.json())
            return {
                "success": False,
                "status_code": response.status_code
            }

        response = response.json()

        return response
    
    @staticmethod
    def getPropertyRentEstimateGeneral(address):
        #   address is required parameter, the format is Street, City, State, Zip
        #   propertyType is optional parameter, example include Single Family
        #   bedrooms is optional parameter, example include 5
        #   bathrooms is optional parameter, example include 4
        #   squareFootage is optional parameter, example include 1600
        #   compCount is optional parameter, it is used to compare compCount number of properties, defaults to 10 if not specified. usually between 5-25
        #   property radius here is 50

        querystring = {
            "address": address,
        }

        response = requests.get(URL, headers=HEADERS, params=querystring)
        print(response)
        if response.status_code != 200:
            print("getPropertyRentEstimate response: ", response.json())
            return {"status_code": response.status_code , "message": response.json()}

        response = response.json()
        response["status_code"] = 200
        return response
