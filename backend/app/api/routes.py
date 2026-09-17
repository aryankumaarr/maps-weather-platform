from fastapi import APIRouter
# APIRouter is a FastAPI class used to organize API endpoints in separate files

from app.schemas.route import RouteRequest
# Imports our RouteRequest model from app/schemas/route.py to validate incoming route data

from app.services.route_service import get_route_data
# Imports the routing function from the route service

router = APIRouter()
# Creates a router object where we can register route-related API endpoints

# Registers this function as a POST endpoint at /route
@router.post("/route")
def get_route(request: RouteRequest):
   #sends the validated coordinates to the route service
   route = get_route_data(request.origin, request.destination)

     # Returns the stable Day 2 response contract for the frontend.
   return {
        "route": route,
        "weather_analysis": {
            "overall_risk": "moderate",
            "conditions": []
        },
        "alternative_route": None,
        "recommendation": "normal_route"
           }