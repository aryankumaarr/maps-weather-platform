# APIRouter is a FastAPI class used to organize API endpoints in separate files
from fastapi import APIRouter

from app.schemas.route import RouteRequest

# Imports our RouteRequest model to validate incoming route data
from app.services.route_service import get_route_data

# Imports the routing analysis so the API can analyze weather along the route
from app.services.routing_analysis import analyze_route_weather

router = APIRouter()


# Registers this function as a POST endpoint at /route
@router.post("/route")
def get_route(request: RouteRequest):
    # Sends the validated coordinates to the route service
    route = get_route_data(request.origin, request.destination)

    # Analyzes weather along the route and creates a routing recommendation
    analysis = analyze_route_weather(route)

    # Returns the Day 2 response contract using the routing analysis results
    return {
        "route": route,
        "weather_analysis": {
            "overall_risk": analysis["overall_risk"],
            "conditions": [],
        },
        "alternative_route": analysis["alternative_route"],
        "recommendation": analysis["recommendation"],
        "reason": analysis["reason"],
    }