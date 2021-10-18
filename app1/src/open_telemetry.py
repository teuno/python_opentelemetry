from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor


def add_instumentation(app):
    FlaskInstrumentor().instrument_app(app)
    RequestsInstrumentor().instrument()
    # breaks on double quote in logs
    format = "{\"log_type\": \"application_log\", \"time\":\"%(asctime)s\"," \
             " \"level\": \"%(levelname)s\", \"file_location\": \"%(filename)s:%(lineno)d\"," \
             "  \"message\": \"%(message)s\" , \"trace_id\": \"%(otelTraceID)s\"," \
             " \"span_id\": \"%(otelSpanID)s\", \"resource.service.name\": \"%(otelServiceName)s\"}"

    LoggingInstrumentor().instrument(set_logging_format=True, logging_format=format)

