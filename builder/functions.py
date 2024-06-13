from hotel.functions import get_hotels
from transport.functions import get_transport
from transport.query import get_transport_type_name_by_id
from weather.functions import get_weather


async def build_routes(routes_data):
    routes = []
    for route_data in routes_data:
        origin = route_data.get('origin')
        destination = route_data.get('destination')
        date = route_data.get('date')
        preferred_transport = route_data.get('preferred_transport', [])

        # Получаем информацию о маршруте между городами с учетом предпочтительных видов транспорта
        route = await build_route(origin, destination, date, preferred_transport)
        routes.append(route)

    return {"routes": routes}


async def build_route(origin, destination, date, preferred_transport):
    transport = await get_transport(origin, destination, date, preferred_transport)
    transport_name = await get_transport_type_name_by_id(transport.id) if transport else None
    hotels = await get_hotels(destination, date)
    weather = await get_weather(destination, date)

    return {
        "origin": origin,
        "destination": destination,
        "transport": transport_name,
        "hotels": hotels,
        "weather": weather
    }
