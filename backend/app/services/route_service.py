
# Handles routing logic separately from the API endpoint
def get_route_data(origin, destination):
    # Converts Pydantic coordinate objects into regular dictionaries
    origin = origin.model_dump()
    destination = destination.model_dump()

    # Uses mock route data for Day 2.
    return {
        "distance_km": 300.5,
        "duration_minutes": 185,
        "polyline": "mock_polyline",
        # Mock segments represent locations along the route where weather can be checked
        "segments": [
            {
                "start": origin,
                "end": {"lat": 52.2681, "lng": -113.8112},
            },
            {
                "start": {"lat": 52.2681, "lng": -113.8112},
                "end": destination,
            },
        ],
    }