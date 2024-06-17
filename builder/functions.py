from quart import json

from city.functions import get_city_name
from hotel.functions import get_hotels
from transport.functions import get_transport
from weather.functions import get_weather


async def build_routes(data):
    city_departure = await get_city_name(data["city_departure"])
    city_arrival = await get_city_name(data["city_arrival"])
    date_arrival = data["date_arrival"]
    date_left = data["date_left"]
    transport = [data["transport"]]

    weather_data = await get_weather(city_arrival)

    transport_data = await get_transport(city_departure, city_arrival, date_arrival, transport)
    transformed_transport_data = [
        {
            "price": item["price"],
            "departure_datetime": item["departure_datetime"],
            "arrival_datetime": item["arrival_datetime"]
        }
        for item in transport_data
    ]

    hotels_data = get_hotels(city_arrival, date_arrival, date_left)

    response = {
        "weather": weather_data,
        "transport": transformed_transport_data,
        "hotels": hotels_data
    }

    response_json = json.dumps(response, ensure_ascii=False)
    return response_json
