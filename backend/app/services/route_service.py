# Handles routing logic separately from the API endpoint.
def get_route_data(origin, destination):
     # Uses mock route data 
    return{
        "distance_km": 300.5,
        "duration_minutes":185 ,
        "polyline": "mock_polyline" ,
        "segments": []
    }