# syntax=docker/dockerfile:1

FROM python:3.8
WORKDIR /src

COPY ./app/ app/
COPY ./Pipfile* ./

RUN python3 -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy

EXPOSE 8000

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]