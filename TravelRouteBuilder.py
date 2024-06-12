import asyncio
from quart import Quart, request, jsonify
from hypercorn.config import Config
from hypercorn.asyncio import serve
from quart_cors import cors
import logging
from logging import INFO

from builder.functions import build_routes
from models.models import *
from sqlalchemy import create_engine
from config.db_config import db_url


logger = logging.getLogger()

engine = create_engine(db_url)
Base.metadata.create_all(bind=engine)


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
    allow_origin=["http://UI:2000"], #TODO добавить адреса, откуда разрешено принимать запросы
    allow_credentials=True,  # Разрешить использование куки
    allow_methods=["GET", "POST", "OPTIONS", "PUT", "DELETE"],  # Разрешенные методы
    allow_headers=["Content-Type", "Authorization"],  # Разрешенные заголовки
)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 30 МБ


@app.route('/travel_route', methods=['POST'])
async def get_route():
    try:
        data = await request.json
        routes_data = data.get('routes')
        if not routes_data:
            return jsonify("Не найдены маршруты в данных"), 400

        # Строим маршруты между городами для каждого маршрута
        routes = await build_routes(routes_data)

        return jsonify(routes), 200

    except Exception as e:
        response = "Ошибка при обработке запроса"
        return jsonify(response), 400


if __name__ == "__main__":
    __config_logger()
    config = Config()
    config.bind = ["0.0.0.0:1488"]
    config.scheme = "http"
    asyncio.run(serve(app, config))
