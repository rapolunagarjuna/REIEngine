from constants.urls import URLS, mortgageEndpoints, financeEndpoints
from constants.urls import REALTY_API_KEY
import requests

# Store it via KMS in future 
APIKEY = REALTY_API_KEY
HOST = "realty-in-us.p.rapidapi.com"

class MFToolService:

    @staticmethod
    def checkRates(params):
        url = URLS.get("realtyUS")
        response = requests.get(
            f"{url}/{mortgageEndpoints.get('checkRates')}",
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
        print("mortgate checkRates response: ", response)
        return response
    
    @staticmethod
    def calculate(params):
        url = URLS.get("realtyUS")
        response = requests.get(
            f"{url}/{mortgageEndpoints.get('calculate')}",
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
        print("mortgate calculate response: ", response)
        return response
    

    @staticmethod
    def calculateAffordability(params):
        url = URLS.get("realtyUS")
        response = requests.get(
            f"{url}/{mortgageEndpoints.get('calculateAffordability')}",
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
        print("calculateAffordability response: ", response)
        return response
    

    @staticmethod
    def checkEquityRates(params):
        url = URLS.get("realtyUS")
        response = requests.get(
            f"{url}/{mortgageEndpoints.get('checkEquityRates')}",
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
        print("checkEquityRates response: ", response)
        return response
    

    @staticmethod
    def financeRates(params):
        url = URLS.get("realtyUS")
        response = requests.get(
            f"{url}/{financeEndpoints.get('rates')}",
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
        print("financeRates response: ", response)
        return response