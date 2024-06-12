# Используем официальный образ Python в качестве основы
FROM python:3.10

# Установим рабочую директорию в контейнере
WORKDIR /app

# Скопируем зависимости проекта в контейнер
COPY requirements.txt .

# Установим зависимости
RUN pip install -r requirements.txt

# Скопируем все файлы проекта в контейнер
COPY . .

# Команда для запуска приложения
CMD ["python", "TravelRouteBuilder.py"]

# Откроем порт для внешних подключений
EXPOSE 1488

# docker build -t TravelRouteBuilder .
# docker run -p 1488:1488 --name TravelRouteBuilder --network huyandeks_network TravelRouteBuilder