#!/bin/bash

echo "Setting environment variables for OpenTelemetry..."
export OTEL_LOGS_EXPORTER=otlp
export OTEL_METRICS_EXPORTER=otlp
export OTEL_TRACES_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
export FLASK_APP=app.py

echo "Starting instrumented Flask application..."
opentelemetry-instrument \
  --logs_exporter otlp \
  --metrics_exporter otlp \
  --traces_exporter otlp \
  --service_name jithin-monolith-app \
  python -m flask run -p 8081
