from constants.urls import URLS, schoolsEndpoints
import requests

# Store it via KMS in future 
APIKEY = 'b5d50eadecmshae6f3750c658061p1f6953jsnbf3a1e1a21b1'
HOST = "realty-in-us.p.rapidapi.com"

class SchoolsService:

    @staticmethod
    def getSchoolsList(params):
        url = URLS.get("realtyUS")
        response = requests.get(
            f"{url}/{schoolsEndpoint.get('list')}",
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
        print("getSchoolsList response: ", response)
        return response
    
    @staticmethod
    def getSchoolsDetail(params):
        url = URLS.get("realtyUS")
        response = requests.get(
            f"{url}/{schoolsEndpoint.get('detail')}",
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
        print("getSchoolsDetail response: ", response)
        return response
    
    @staticmethod
    def getSchoolsDistrict(params):
        url = URLS.get("realtyUS")
        response = requests.get(
            f"{url}/{schoolsEndpoint.get('getSchoolDistrict')}",
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
        print("getSchoolsDistrict response: ", response)
        return response