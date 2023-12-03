from constants.urls import URLS
from constants.urls import agentEndpoints
from constants.urls import REALTY_API_KEY
import requests

# Store it via KMS in future 
APIKEY = REALTY_API_KEY
HOST = "realty-in-us.p.rapidapi.com"
HEADERS = {
    'X-RapidAPI-Key': APIKEY,
    'X-RapidAPI-Host': HOST
}
URL = URLS.get("realtyUS")

class AgentService:

    @staticmethod
    def getAgentList(params):
        response = requests.get(
            f"{URL}/{agentEndpoints.get('agentList')}",
            headers=HEADERS,
            params=params
        )

        if response.status_code != 200:
            return {
                "success": False,
                "status_code": response.status_code
            }
        
        response = response.json()
        print("getAgentList response: ", response)
        
        return response
    
    @staticmethod
    def getAgentProfile(params):
        response = requests.get(
            f"{URL}/{agentEndpoints.get('agentProfile')}",
            headers=HEADERS,
            params=params
        )

        if response.status_code != 200:
            return {
                "success": False,
                "status_code": response.status_code
            }
        
        response = response.json()
        print("getAgentProfile response: ", response)
        return response
    
    @staticmethod
    def getAgentReviews(params):
        response = requests.get(
            f"{URL}/{agentEndpoints.get('agentReviews')}",
            headers=HEADERS,
            params=params
        )

        if response.status_code != 200:
            return {
                "success": False,
                "status_code": response.status_code
            }
        
        response = response.json()
        print("getAgentReviews response: ", response)
        return response
    
    @staticmethod
    def getAgentRecommendations(params):
        response = requests.get(
            f"{URL}/{agentEndpoints.get('agentRecommendations')}",
            headers=HEADERS,
            params=params
        )

        if response.status_code != 200:
            return {
                "success": False,
                "status_code": response.status_code
            }
        
        response = response.json()
        print("getAgentRecommendations response: ", response)
        return response
    
    @staticmethod
    def getAgentListings(params):
        response = requests.get(
            f"{URL}/{agentEndpoints.get('agentListings')}",
            headers=HEADERS,
            params=params
        )

        if response.status_code != 200:
            return {
                "success": False,
                "status_code": response.status_code
            }
        
        response = response.json()
        print("getAgentListings response: ", response)
        return response