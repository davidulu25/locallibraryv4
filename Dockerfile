# FROM python:3
FROM python:3-slim-bullseye
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8000
EXPOSE 8000
ENV PYTHONUNBUFFERED=1