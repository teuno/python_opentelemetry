from opentelemetry import trace
from opentelemetry.exporter.zipkin.proto.http import ZipkinExporter
from opentelemetry.propagate import set_global_textmap
from opentelemetry.propagators.b3 import B3MultiFormat

from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

bind = "0.0.0.0:8002"
workers = 2
threads = 2

accesslog = "-"
errorlog = "-"
loglevel = "info"
# breaks on double quote in logs
access_log_format = (
    "{\"log_type\": \"access_log\", \"ip\": \"%(h)s\", \"request_method\": \"%(m)s\", \"url_path\": \"%(U)s\","
    "  \"protocol\": \"%(H)s\", \"user_agent\": \"%(a)s\", \"request_time_ms\": \"%(M)s\", "
    "\"status_code\": \"%(s)s\", \"query_parameters\": \"%(q)s\",\"request_date\": \"%(t)s\", "
    "\"response_size\": \"%(B)s\" }")

# docker specific requirements
worker_tmp_dir = "/dev/shm"
worker_class = "gthread"


# when it's here we don't need it in the app itself
def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)

    trace.set_tracer_provider(
        TracerProvider(
            resource=Resource.create({SERVICE_NAME: "app3-aws-s3"})
        )
    )

    zipkin_exporter = ZipkinExporter(
        endpoint="http://zipkin:9411/api/v2/spans",
    )

    trace.get_tracer_provider().add_span_processor(
        BatchSpanProcessor(zipkin_exporter)
    )

    set_global_textmap(B3MultiFormat())
