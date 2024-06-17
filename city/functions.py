import aiohttp
from config.enviroment import city_url


async def get_city_name(city_id):
    url = city_url + f'/{city_id}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # Проверяем статус ответа
            if response.status == 200:
                # Декодируем JSON из ответа (асинхронно)
                data = await response.json()
                # Получаем значение 'name' из JSON
                city_name = data['name']
                return city_name
            else:
                # Обрабатываем случай ошибки HTTP, например:
                raise ValueError(f"Failed to fetch data: {response.status}")
