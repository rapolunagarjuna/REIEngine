from constants.urls import URLS, propertyEndpoints
import requests

# Store it via KMS in future 
APIKEY = 'b5d50eadecmshae6f3750c658061p1f6953jsnbf3a1e1a21b1'
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
            return {
                "success": False,
                "status_code": response.status_code
            }
        
        response = response.json()
        print("getPropertyDetails response: ", response)
        return response
    
    @staticmethod
    def getPropertyList(params):
        url = URLS.get("realtyUS")
        response = requests.post(
            f"{url}/{propertyEndpoints.get('list')}",
            headers={
                'content-type': 'application/json',
                'X-RapidAPI-Key': APIKEY,
                'X-RapidAPI-Host': HOST
            },
            json={
                "limit": 200,
                "offset": 0,
                "postal_code": '02125',
                "status": [
                    'for_sale',
                    'ready_to_build'
                ],
                "sort": {
                    "direction": 'desc',
                    "field": 'list_date'
                }
            } #params
        )

        if response.status_code != 200:
            return {
                "success": False,
                "status_code": response.status_code
            }
        
        response = response.json()
        print("getPropertyList response: ", response)
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
        
        response = response.json()
        print("getSimilarPropertyList response: ", response)
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
        
        response = response.json()
        print("getPropertyPhotos response: ", response)
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
        
        response = response.json()
        print("getPropertyPhotos response: ", response)
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
        
        response = response.json()
        print("getPropertyPhotos response: ", response)
        return response