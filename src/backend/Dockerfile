FROM python:3.10-alpine as base
WORKDIR /code
RUN apk add --update --virtual .build-deps \
    build-base \
    postgresql-dev \
    python3-dev \
    libpq

COPY requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

FROM python:3.10-alpine as production
WORKDIR /code
RUN apk add libpq
COPY --from=base /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/
COPY app /code/app
ENV PYTHONUNBUFFERED 1