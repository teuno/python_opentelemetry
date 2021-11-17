import logging

import requests
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
from opentelemetry import trace

from open_telemetry import add_instumentation

logger = logging.getLogger(__name__)
tracer = trace.get_tracer(__name__)


def create_app():
    app = Flask(__name__)
    metrics = PrometheusMetrics.for_app_factory()
    metrics.init_app(app)
    add_instumentation(app)

    @app.route("/")
    def hello():
        logger.info("hoi form function")
        requests.get("https://google.com")
        with tracer.start_as_current_span("example-request"):
            requests.get("https://example.com")

        response1 = requests.get("http://app2:8001")
        response2 = requests.get("http://app3:8002")

        response = f"{response1.text} <br> {response2.text}"

        return response

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
