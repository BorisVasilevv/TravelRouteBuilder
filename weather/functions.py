from config.enviroment import weather_api_key


async def fetch_weather(session, city_name):
    base_url = "https://api.weatherapi.com/v1/forecast.json"

    # Make a request to the API
    params = {
        'key': weather_api_key,
        'q': city_name,
        'days': 1
    }

    async with session.get(base_url, params=params) as response:
        data = await response.json()
        return data
