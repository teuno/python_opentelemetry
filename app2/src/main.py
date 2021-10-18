import logging

from flask import Flask
from opentelemetry import trace
from sqlalchemy import create_engine

from open_telemetry import add_instumentation

tracer = trace.get_tracer(__name__)
logger = logging.getLogger(__name__)


db_password = "Jt567Y2"
db_user = "my_user"
db_hostname = "postgres"


def create_app():
    app = Flask(__name__)
    engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_hostname}/postgres")
    add_instumentation(app, engine)

    @app.route("/")
    def hello():
        logger.info("test my' logging")
        with engine.connect() as connection:
            rs = connection.execute("select username from test_schema.users")
            result = [row[0] for row in rs]

        return str(result)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
