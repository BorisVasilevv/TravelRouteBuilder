import aiohttp
from config.enviroment import hotel_url


async def get_hotels(city, date):
    url = hotel_url
    headers = {'Content-Type': 'application/json'}
    payload = {
        "city": city,
        "date": date
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            return await response.json()
