FROM python:3

ENV APP /app

RUN mkdir $APP
WORKDIR $APP

EXPOSE 5000

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY health.ini ./health.ini
COPY health_app ./health_app

CMD ["uwsgi", "--ini", "health.ini"]