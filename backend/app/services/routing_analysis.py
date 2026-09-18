# Gets weather using coordinates so weather can be checked along the route.
from app.services.weather_service import get_weather_data


# Analyzes weather conditions along a route and returns a routing recommendation.
def analyze_route_weather(route):
    # Stores route segments where dangerous weather is detected.
    affected_segments = []

    # Loops through each segment so rerouting is not based only on destination weather.
    for segment in route["segments"]:
        coordinate = segment["end"]

        # Gets weather for a coordinate along the route.
        segment_weather = get_weather_data(
            coordinate["lat"],
            coordinate["lng"],
        )

        # Uses simple rule-based logic instead of AI/ML.
        if segment_weather["condition"] == "snow":
            affected_segments.append(segment)

    # If dangerous weather was found anywhere along the route, recommend the mock alternative.
    if affected_segments:
        return {
            "overall_risk": "high",
            "affected_segments": affected_segments,
            "alternative_route": {
                "distance_km": 310.2,
                "duration_minutes": 192,
                "polyline": "mock_alternative_polyline",
            },
            "recommendation": "alternative_route",
            "reason": "Snow detected along the original route.",
        }

    # If no dangerous condition is found along the route, keep the original route.
    return {
        "overall_risk": "low",
        "affected_segments": [],
        "alternative_route": None,
        "recommendation": "normal_route",
        "reason": "No dangerous weather detected along the original route.",
    }