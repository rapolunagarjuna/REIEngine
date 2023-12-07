from constants.urls import URLS, propertyEndpoints
from constants.urls import REALTY_API_KEY
import requests

# Store it via KMS in future 
APIKEY = REALTY_API_KEY
HOST = "realty-in-us.p.rapidapi.com"

class PropertyService:

    @staticmethod
    def getPropertyDetails(params):
        url = URLS.get("realtyUS")
        response = requests.get(
            f"{url}/{propertyEndpoints.get('details')}",
            headers={
                'X-RapidAPI-Key': APIKEY,
                'X-RapidAPI-Host': HOST
            },
            params=params
        )

        if response.status_code != 200:
            print("getPropertyDetails response status code:", response.status_code)
            print(response.content)

            return {
                "success": False,
                "status_code": response.status_code
            }
        print("getPropertyDetails response status code:", response.status_code)
        
        response = response.json()
        return response
    
    @staticmethod
    def getPropertyList(params):
        city = params.get("city")
        state_code = params.get("stateCode")
        postal_code = params.get("postalCode")

        url = URLS.get("realtyUS")
        data = {
            "limit": 200,
            "offset": 0,
            "status": [
                'for_sale',
                'ready_to_build'
            ],
            "sort": {
                "direction": 'desc',
                "field": 'list_date'
            }
        }

        if postal_code:
            data["postal_code"] = postal_code
        else:
            data["city"] = city
            data["state_code"] = state_code

        response = requests.post(
            f"{url}/{propertyEndpoints.get('list')}",
            headers={
                'content-type': 'application/json',
                'X-RapidAPI-Key': APIKEY,
                'X-RapidAPI-Host': HOST
            },
            json=data
        )

        if response.status_code != 200:
            return {
                "success": False,
                "status_code": response.status_code
            }
        print("getPropertyList response status code:", response.status_code)
        response = response.json()
        
        return response


    @staticmethod
    def getSimilarPropertyList(params):
        url = URLS.get("realtyUS")
        response = requests.get(
            f"{url}/{propertyEndpoints.get('listSimilar')}",
            headers={
                'X-RapidAPI-Key': APIKEY,
                'X-RapidAPI-Host': HOST
            },
            params=params
        )

        if response.status_code != 200:
            return {
                "success": False,
                "status_code": response.status_code
            }
        print("getSimilarPropertyList response status code:", response.status_code)
        
        response = response.json()
        return response

    @staticmethod
    def getPropertyPhotos(params):
        url = URLS.get("realtyUS")
        response = requests.get(
            f"{url}/{propertyEndpoints.get('getPhotos')}",
            headers={
                'X-RapidAPI-Key': APIKEY,
                'X-RapidAPI-Host': HOST
            },
            params=params
        )

        if response.status_code != 200:
            return {
                "success": False,
                "status_code": response.status_code
            }
        print("getPropertyPhotos response status code:", response.status_code)
        
        response = response.json()
        return response
    
    @staticmethod
    def getCommuteTime(params):
        url = URLS.get("realtyUS")
        response = requests.get(
            f"{url}/{propertyEndpoints.get('getCommuteTime')}",
            headers={
                'X-RapidAPI-Key': APIKEY,
                'X-RapidAPI-Host': HOST
            },
            params={
                "destination_address": '1 South point drive, Dorchester',
                "property_id": "1509681899",
                "transportation_type": 'walking',
                "with_traffic": 'false'
            }
        )

        if response.status_code != 200:
            return {
                "success": False,
                "status_code": response.status_code
            }
        print("getCommuteTime response status code:", response.status_code)
        
        response = response.json()
        return response


    @staticmethod
    def getSurroundings(params):
        url = URLS.get("realtyUS")
        response = requests.get(
            f"{url}/{propertyEndpoints.get('getSurroundings')}",
            headers={
                'X-RapidAPI-Key': APIKEY,
                'X-RapidAPI-Host': HOST
            },
            params={
                "property_id": "1509681899",
                "enable_flood": 'false'
            }
        )

        if response.status_code != 200:
            return {
                "success": False,
                "status_code": response.status_code
            }
        print("getSurroundings response status code:", response.status_code)
        
        response = response.json()
        return response