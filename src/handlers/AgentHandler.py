from flask import Blueprint, request, jsonify
from src.services.AgentService import AgentService

agent = Blueprint("agent", __name__, url_prefix="/agent")


@agent.route("/list", methods=['GET'])
def getAgentList():
    params = request.args
    print("Params for getAgentList",params)

    agentlist = AgentService.getAgentList(params)
    return jsonify(agentlist)

@agent.route("/get-profile", methods=['GET'])
def getAgentProfile():
    params = request.args
    print("Params for getAgentProfile",params)

    agentProfile = AgentService.getAgentProfile(params)
    return jsonify(agentProfile)

@agent.route("/get-reviews", methods=['GET'])
def getAgentReviews():
    params = request.args
    print("Params for getAgentReviews",params)

    agentReviews = AgentService.getAgentReviews(params)
    return jsonify(agentReviews)

@agent.route("/get-recommendations", methods=['GET'])
def getAgentRecommendations():
    params = request.args
    print("Params for getAgentRecommendations",params)

    agentReccommendations = AgentService.getAgentRecommendations(params)
    return jsonify(agentReccommendations)

@agent.route("/get-listings", methods=['GET'])
def getAgentListings():
    params = request.args
    print("Params for getAgentListings",params)

    agentListings = AgentService.getAgentListings(params)
    return jsonify(agentListings)