FROM python:2.7-alpine

EXPOSE 8887

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    postgresql-dev \
    python-dev \
    && pip install --no-cache-dir -Iv psycopg2==2.7.6.1 \
    && apk add --no-cache postgresql-client \
    && apk del --no-cache .build-deps

ADD app/lib /app/lib/
WORKDIR /app/lib/pushkin

RUN python setup.py install

WORKDIR /app

ADD app /app

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]

CMD ["pushkin", "--configuration", "/app/pushkinconfig.ini"]
