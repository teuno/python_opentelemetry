from opentelemetry.instrumentation.botocore import BotocoreInstrumentor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor


def add_instumentation(app):
    FlaskInstrumentor().instrument_app(app)
    BotocoreInstrumentor().instrument()
    # how to stop multiline logs with exception ( did not work yet):
    # https://stackoverflow.com/questions/48642111/can-i-make-python-output-exceptions-in-one-line-via-logging
    # breaks on double quote in logs
    format = "{\"log_type\": \"application_log\", \"time\":\"%(asctime)s\"," \
             " \"level\": \"%(levelname)s\", \"file_location\": \"%(filename)s:%(lineno)d\"," \
             "  \"message\": \"%(message)s\" , \"trace_id\": \"%(otelTraceID)s\"," \
             " \"span_id\": \"%(otelSpanID)s\", \"resource.service.name\": \"%(otelServiceName)s\"}"

    LoggingInstrumentor().instrument(set_logging_format=True, logging_format=format)