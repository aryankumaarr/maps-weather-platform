# Handles weather logic separately from the API and routing code.
def get_weather_data(lat, lng):
    # Uses mock weather data for Day 2
    return {
        "latitude": lat,
        "longitude": lng,
        "condition": "snow",
        "temperature_c": -5,
        "wind_speed_kmh": 25,
        "visibility_km": 4,
    }