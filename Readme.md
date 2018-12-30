# How to run [pushkin.io](https://github.com/Nordeus/pushkin) in Docker

This is an example of running [pushkin.io](https://github.com/Nordeus/pushkin) on Docker and docker-compose

## Explanation
I had to build pushkin from source code instead of using binary because there was no support for environment variables in config `pushkinconfig.ini` file. To enable environment variables I had to modify one line in `lib/pushkin/pushkin/config.py:77` and then you can set e.g. `db_port = %(PGPORT)s` in the config file instead of hardcoding valus in Docker image.

## Step 1: Generate a correct APN certificate

Follow steps from the pushkin documentation [Setup certificates](http://docs.pushkin.io/en/latest/certificates/) and replace the `certs\apn_push\app_push_dev.pem` file.

## Step 2: Run docker-compose

In the root catalog (where the `docker-compose.yml` file is) run command
```
docker-compose up -d --build
```
this will build docker images (including postgres DB) and create docker containers. 

Verify the `pushkin.api` container is up and running: `docker ps`. It should run on port 44001.

## Step 3: Open a web browser

Open http://localhost:44001/get_request_queue to confirm the app is running correctly.

## Step 4: Verify database

Verify that `pushkin` database was created in `db.postgres` container.
