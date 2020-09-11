FROM python:3
# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
LABEL key="yaus-api" 

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip3 install -r requirements.txt



# COPY ./requirements.txt /requirements.txt
# RUN adduser -D user
# USER user

CMD python manage.py runserver 0.0.0.0:$PORT