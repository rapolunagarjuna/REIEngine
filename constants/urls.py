
URLS = {
    "realtyUS": "https://realty-in-us.p.rapidapi.com"
}

REALTY_API_KEY = "b52991bf0fmsh814fd63a50b2550p116e59jsn3feaf5366b04"

PROPERTY_V3_ROUTE = "properties/v3"
MORTGAGE_V2_ROUTE = "mortgage/v2"
MORTGAGE_V1_ROUTE = "mortgage"
FINANCE_V1_ROUTE = "finance"
AGENT_V1_ROUTE = "agent"
SCHOOLS_V1_ROUTE = "finance"

propertyEndpoints = {
    "details": f"{PROPERTY_V3_ROUTE}/detail",
    "list": f"{PROPERTY_V3_ROUTE}/list",
    "listSimilar": f"{PROPERTY_V3_ROUTE}/list-similar-homes",
    "getPhotos": f"{PROPERTY_V3_ROUTE}/get-photos",
    "getCommuteTime": f"{PROPERTY_V3_ROUTE}/get-commute-time",
    "getSurroundings": f"{PROPERTY_V3_ROUTE}/get-surroundings"
}

mortgageEndpoints = {
    "checkRates": f"{MORTGAGE_V2_ROUTE}/check-rates",
    "calculate": f"{MORTGAGE_V2_ROUTE}/calculate",
    
    "calculateAffordability": f"{MORTGAGE_V1_ROUTE}/calculate-affordability",
    "checkEquityRates": f"{MORTGAGE_V1_ROUTE}/check-equity-rates",
}

financeEndpoints = {
    "rates": f"{FINANCE_V1_ROUTE}/rates",
}

agentEndpoints = {
    "agentList": f"{AGENT_V1_ROUTE}/list",
    "agentProfile":f"{AGENT_V1_ROUTE}/get-profile",
    "agentReviews":f"{AGENT_V1_ROUTE}/get-reviews",
    "agentRecommendations":f"{AGENT_V1_ROUTE}/get-recommendations",
    "agentListings": f"{AGENT_V1_ROUTE}/get-listings"
}

schoolsEndpoints = {
    "list": f"{SCHOOLS_V1_ROUTE}/rates",
    "detail": f"{SCHOOLS_V1_ROUTE}/detail",
    "getSchoolDistrict": f"{SCHOOLS_V1_ROUTE}/get-school-disctict",
}
