# Используем базовый образ Python
FROM python:3.8.10

# Установка переменной окружения PYTHONUNBUFFERED для предотвращения буферизации вывода
ENV PYTHONUNBUFFERED 1

# Создание и установка рабочего каталога внутри контейнера
RUN mkdir /app
WORKDIR /app

# Копирование зависимостей и установка их через pip
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копирование остального кода проекта в рабочий каталог контейнера
COPY . /app/

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
