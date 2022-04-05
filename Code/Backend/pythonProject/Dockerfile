# syntax=docker/dockerfile:1

FROM python:3.7-slim-buste
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "manage.py" , "test", "product.test", "-v 2"]
