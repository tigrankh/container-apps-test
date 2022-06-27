# syntax=docker/dockerfile:1

FROM python:3.8
WORKDIR /src

COPY ./app/ app/
COPY ./Pipfile* ./

RUN python3 -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy

CMD ["python", "./app/api.py"]