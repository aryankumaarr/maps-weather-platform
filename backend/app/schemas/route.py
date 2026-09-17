from pydantic import BaseModel
# Pydantic is a library that validates and structures data for the API.

# BaseModel provides Pydantic validation; putting it in () means Coordinates inherits from it.
class Coordinates(BaseModel):
    lat: float
    lng: float
# RouteRequest inherits BaseModel and requires origin and destination to follow Coordinates.
class RouteRequest(BaseModel):
    origin: Coordinates
    destination: Coordinates