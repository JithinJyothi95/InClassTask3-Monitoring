# INFO8985 – In-Class Task 3: Observability in a Python Monolith

This repository demonstrates OpenTelemetry instrumentation for a monolithic Flask application. It collects logs, metrics, and traces, and exports them to [SigNoz](https://github.com/SigNoz/signoz) for observability.

---

## Key Features

- Automatic and manual instrumentation using `opentelemetry-instrument`
- Tracks dice rolls via a `/dicetracker` endpoint
- Simulates an error when a 1 is rolled to test exception visibility
- Metrics, logs, and traces are sent using the OTLP exporter
- Visualized in SigNoz via Docker Compose stack

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/JithinJyothi95/InClassTask3-Monitoring.git
cd InClassTask3-Monitoring
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Start SigNoz (in a separate terminal)

```bash
cd signoz/deploy/docker
docker-compose up -d
```

### 4. Run the App with Instrumentation

```bash
chmod +x run_instrumented.sh
./run_instrumented.sh
```

This starts the Flask server on port `8081
` with OpenTelemetry instrumentation enabled.

---

## Test the App

Visit: [http://localhost:8081
/dicetracker?player=jithin](http://localhost:8081/dicetracker?player=jithin)
OR
https://8081-your-username-your-repo-name-xxxxx.github.dev/dicetracker?player=jithin

Each request simulates a dice roll (1–6).  
If the result is `1`, a `ValueError` is triggered and sent to SigNoz as a log and trace.

---

## Files Overview

| File                    | Purpose                                       |
|-------------------------|-----------------------------------------------|
| `app.py`                | Flask app with tracing and metric logic       |
| `run_instrumented.sh`   | Script to set OpenTelemetry env vars and run  |
| `requirements.txt`      | Python dependencies                           |
| `docker-compose.yml`    | For SigNoz stack                              |
| `otel-collector-config.yaml` | OpenTelemetry Collector configuration    |

---

## Screenshots Summary

| Screenshot            | What It Shows                                     |
|-----------------------|----------------------------------------------------|
| services-overview     | `jithin-monolith-app` detected in SigNoz          |
| metric-name-view      | Custom metric `dice.rolls` visible                 |
| metric-graph-view     | Roll count over time (rolling dice requests)       |
| RollValue.png         | Attribute-based metric breakdown by dice value     |
| Logs.png              | General app logs collected in SigNoz              |
| error-logs.png        | Error log (ValueError when roll = 1)               |
| Exception.png         | Exception shown with traceback in SigNoz          |
| terminal-logs.png     | Console log showing real-time trace and logs      |
| trace-span-list.png   | Trace spans captured by OTEL exporter  |

---

## Completed Tasks

- [x] Added manual exception handling inside `/dicetracker`
- [x] Validated logs, traces, and metrics appear in SigNoz
- [x] Used OpenTelemetry instrumentation with custom service name
- [x] Verified exceptions aren't silently swallowed (500 shown in browser)

---

## Notes

- OTLP export is configured via HTTP to `localhost:4318`
- Flask runs on port `8081`
- Bash script simplifies environment setup and run

---

**Author:** Jithin Jyothi  
**Course:** INFO8985  
**Instructor:** Prof. Rhildred  
**Task:** In-Class Task 3