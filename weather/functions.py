import aiohttp
from config.enviroment import weather_url


async def get_weather(city_name):
    url = weather_url + f'/{city_name}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # Проверяем статус ответа
            if response.status == 200:
                return await response.json()
            else:
                # Обрабатываем случай ошибки HTTP, например:
                raise ValueError(f"Failed to fetch data: {response.status}")
