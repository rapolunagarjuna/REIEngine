from flask import Blueprint, request, jsonify
from src.services.AgentService import AgentService

property = Blueprint("agent", __name__, url_prefix="/agent")


@property.route("/list", methods=['GET'])
def getAgentList():
    params = request.args
    print("Params for getAgentList",params)

    agentlist = AgentService.getAgentList(params)
    return jsonify(agentlist)

@property.route("/get-profile", methods=['GET'])
def getAgentProfile():
    params = request.args
    print("Params for getAgentProfile",params)

    agentProfile = AgentService.getAgentProfile(params)
    return jsonify(agentProfile)

@property.route("/get-reviews", methods=['GET'])
def getAgentReviews():
    params = request.args
    print("Params for getAgentReviews",params)

    agentReviews = AgentService.getAgentReviews(params)
    return jsonify(agentReviews)

@property.route("/get-recommendations", methods=['GET'])
def getAgentRecommendations():
    params = request.args
    print("Params for getAgentRecommendations",params)

    agentReccommendations = AgentService.getAgentRecommendations(params)
    return jsonify(agentReccommendations)

@property.route("/get-listings", methods=['GET'])
def getAgentListings():
    params = request.args
    print("Params for getAgentListings",params)

    agentListings = AgentService.getAgentListings(params)
    return jsonify(agentListings)