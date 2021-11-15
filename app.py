import logging
import os

import flask
import toml

# The APP_NAME environment variable sets your app's name.
# Demoapp is for demonstrations where you often run multiple containers
# that have different names. The default name is app.
app = flask.Flask(os.environ.get("APP_NAME", __name__))

# The FLASK_ENV environment variable sets your app's environment.
# The app.config["ENV"] dictionary entry stores the value of your app's environment.
# Refer to https://flask.palletsprojects.com/en/2.0.x/config/#ENV for more details.

# The VERSION.txt file sets your app's version.
with open("VERSION.txt") as fh:
    app.config["VERSION"] = fh.read().strip()

# Your app loads configuration from the config.toml file.
# Refer to https://flask.palletsprojects.com/en/2.0.x/config/#configuring-from-data-files
# for more details.
app.config.from_file(os.environ.get("CONFIG_FILE", "config.toml"), load=toml.load)


@app.route("/")
def default_route():
    app.logger.info(f"Got request from {flask.request.remote_addr}")
    response = {
        "name": app.name,
        "env": app.config["ENV"],
        "version": app.config["VERSION"],
    }
    return flask.jsonify(response)


if __name__ != "__main__":
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
