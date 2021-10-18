import logging
import os
from botocore.session import Session
from flask import Flask

from open_telemetry import add_instumentation

logger = logging.getLogger(__name__)


access_key = os.environ.get("AWS_ACCESS_KEY", "")
secret_key = os.environ.get("AWS_SECRET_KEY", "")

session = Session()
session.set_credentials(
    access_key=access_key, secret_key=secret_key
)
s3_client = session.create_client("s3", region_name="eu-west-2")


def create_app():
    app = Flask(__name__)
    add_instumentation(app)

    @app.route("/")
    def hello():
        logger.info(f"my secret = ${access_key}")

        response = s3_client.list_buckets()
        return response

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
