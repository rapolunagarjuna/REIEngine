
URLS = {
    "realtyUS": "https://realty-in-us.p.rapidapi.com"
}

PROPERTY_V3_ROUTE = "properties/v3"
MORTGAGE_V2_ROUTE = "mortgage/v2"
MORTGAGE_V1_ROUTE = "mortgage"
FINANCE_V1_ROUTE = "finance"
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

schoolsEndpoints = {
    "list": f"{SCHOOLS_V1_ROUTE}/rates",
    "detail": f"{SCHOOLS_V1_ROUTE}/detail",
    "getSchoolDistrict": f"{SCHOOLS_V1_ROUTE}/get-school-disctict",
}