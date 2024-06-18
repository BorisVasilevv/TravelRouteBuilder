from city.functions import get_city_name
from hotel.functions import get_hotels
from transport.functions import get_transport
from weather.functions import get_weather


async def build_routes(data):
    try:
        city_departure = await get_city_name(data["city_departure"])
    except Exception as e:
        raise ValueError(f"Failed to get city name for departure: {e}")

    try:
        city_arrival = await get_city_name(data["city_arrival"])
    except Exception as e:
        raise ValueError(f"Failed to get city name for arrival: {e}")

    date_arrival = data["date_arrival"]
    date_left = data["date_left"]
    transport = data["transport"]

    try:
        weather_data = await get_weather(city_arrival)
    except Exception as e:
        raise ValueError(f"Failed to get weather data: {e}")

    try:
        transport_data = await get_transport(city_departure, city_arrival, date_arrival, transport)
        transformed_transport_data = [
            {
                "price": item["price"],
                "departure_datetime": item["departure_datetime"],
                "arrival_datetime": item["arrival_datetime"]
            }
            for item in transport_data
        ]
    except Exception as e:
        raise ValueError(f"Failed to get transport data: {e}")

    try:
        hotels_data = await get_hotels(city_departure, date_arrival, date_left)
    except Exception as e:
        raise ValueError(f"Failed to get hotels data: {e}")

    response = {
        "weather": weather_data,
        "transport": transformed_transport_data,
        "hotels": hotels_data
    }

    return response
