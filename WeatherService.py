import asyncio

import aiohttp
from quart import Quart, request, jsonify
from hypercorn.config import Config
from hypercorn.asyncio import serve
from quart_cors import cors
import logging
from logging import INFO

from weather.functions import fetch_weather

logger = logging.getLogger()


def __config_logger():
    file_log = logging.FileHandler('TravelRouteService.log')
    console_log = logging.StreamHandler()
    FORMAT = '[%(levelname)s] %(asctime)s : %(message)s | %(filename)s'
    logging.basicConfig(level=INFO,
                        format=FORMAT,
                        handlers=(file_log, console_log),
                        datefmt='%d-%m-%y - %H:%M:%S')


app = Quart(__name__)
app = cors(
    app,
    allow_origin=["http://UI:2000"],  # TODO добавить адреса, откуда разрешено принимать запросы
    allow_credentials=True,  # Разрешить использование куки
    allow_methods=["GET", "POST", "OPTIONS", "PUT", "DELETE"],  # Разрешенные методы
    allow_headers=["Content-Type", "Authorization"],  # Разрешенные заголовки
)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 30 МБ


@app.route('/weather/<string:city_name>', methods=['GET'])
async def get_weather(city_name):
    async with aiohttp.ClientSession() as session:
        weather_data = await fetch_weather(session, city_name)
        return weather_data


if __name__ == "__main__":
    __config_logger()
    config = Config()
    config.bind = ["0.0.0.0:7777"]
    config.scheme = "http"
    asyncio.run(serve(app, config))
