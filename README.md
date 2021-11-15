# Demoapp

> Demoapp runs a Flask application that has a single `/` route that returns its name, environment, and version.

## Summary

Demoapp runs as a Docker container in multiple environments. The typical workflows like development and deployment should be clearly documented.

## Quickstart

1. Install dependecies.

   [Docker](https://docs.docker.com/get-docker/) is the only depedency for Demoapp.

1. Get the code.

   ```
   git clone git@github.com:mbigras/demoapp.git
   cd demoapp
   ```

1. Build the Docker image.

   ```
   docker build --tag mbigras/demoapp .
   ```

1. Run the Docker container.

   ```
   docker run --rm --name demoapp --env PORT=8080 --env APP_NAME=foo --env FLASK_ENV=development --publish 8080:8080 mbigras/demoapp
   ```

   The output should look like this:

   ```
   $ docker run --rm --name demoapp --env PORT=8080 --env APP_NAME=foo --env FLASK_ENV=development --publish 8080:8080 mbigras/demoapp
   [2021-11-15 06:22:57 +0000] [1] [INFO] Starting gunicorn 20.1.0
   [2021-11-15 06:22:57 +0000] [1] [INFO] Listening at: http://0.0.0.0:8080 (1)
   [2021-11-15 06:22:57 +0000] [1] [INFO] Using worker: sync
   [2021-11-15 06:22:57 +0000] [9] [INFO] Booting worker with pid: 9
   ```

1. Open a new terminal.

1. Send a GET request.

   ```
   curl http://localhost:8080/
   ```

   The output should look like this:

   ```
   $ curl http://localhost:8080/
   {
     "env": "development",
     "name": "foo",
     "version": "0.1.0"
   }
   ```

1. Shut down demoapp.

   * Press the ctrl-c keyboard shortcut
   * The demoapp Docker container should be removed because you ran the container with the `--rm` option.
