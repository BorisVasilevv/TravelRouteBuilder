# TravelRouteBuilder

## Описание запросов

```/travel_route ['POST']``` Принимает json вида:

```json
{
  "transport": 1,
  "city_departure": 1,
  "city_arrival": 2,
  "date_arrival": "21.05.2022",
  "date_left": "27.05.2022"
}
```

Возвращает json вида:
```json

```
## Команды для разворота в docker

```
git clone https://github.com/BorisVasilevv/weather-service.git //
```

```
cd WetherService
```

```docker build -t travel_route_builder_service .``` // создаем image проекта

```docker run -p 6666:6666 --name travel_route_builder_service travel_route_builder_service``` // создаем docker container

