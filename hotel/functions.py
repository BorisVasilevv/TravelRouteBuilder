import aiohttp
from config.enviroment import hotel_url


async def get_hotels(city, start_date, end_date):
    url = hotel_url
    headers = {'Content-Type': 'application/json'}
    payload = {
        "city": city,
        "start_date": start_date,
        "end_date": end_date
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            return await response.json()
