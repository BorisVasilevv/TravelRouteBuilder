from sqlalchemy.orm import sessionmaker
from TravelRouteBuilder import engine
from models.models import TransportType


# Создание фабрики сессий на основе engine

Session = sessionmaker(bind=engine)


async def get_transport_type_name_by_id(transport_type_id):
    async with Session() as session:
        # Запрос к базе данных для получения объекта типа транспорта по его идентификатору
        transport_type = session.query(TransportType).filter_by(id=transport_type_id).first()

        # Если объект найден, возвращаем его название, иначе возвращаем None
        return transport_type.name if transport_type else None
