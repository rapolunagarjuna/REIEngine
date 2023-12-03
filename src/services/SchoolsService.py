from constants.urls import URLS, schoolsEndpoints
from constants.urls import REALTY_API_KEY
import requests

# Store it via KMS in future 
APIKEY = REALTY_API_KEY
HOST = "realty-in-us.p.rapidapi.com"

class SchoolsService:

    @staticmethod
    def getSchoolsList(params):
        url = URLS.get("realtyUS")
        response = requests.get(
            f"{url}/{schoolsEndpoints.get('list')}",
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
            f"{url}/{schoolsEndpoints.get('detail')}",
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
            f"{url}/{schoolsEndpoints.get('getSchoolDistrict')}",
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