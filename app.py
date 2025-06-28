from flask import Flask, request, redirect
from random import randint
import logging

from opentelemetry import trace, metrics
from opentelemetry.trace import Status, StatusCode

# Telemetry initialization
telemetry_tracer = trace.get_tracer("jithin.monitoring.tracer")
telemetry_meter = metrics.get_meter("jithin.monitoring.meter")

# Defining a custom metric to count rolls
dice_rolls_metric = telemetry_meter.create_counter(
    "dice_rolls_total",
    description="Count of dice rolls by value",
)

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("dice-tracker")

@app.route("/")
def home():
    return redirect("/dicetracker")

@app.route("/dicetracker")
def dice_roll():
    with telemetry_tracer.start_as_current_span("dice_roll_span") as span:
        username = request.args.get('player', default="guest", type=str)
        try:
            rolled_value = roll_dice_logic()
            span.set_attribute("dice.value", rolled_value)
            dice_rolls_metric.add(1, {"dice.value": str(rolled_value)})

            log.info("User %s got a roll of: %s", username, rolled_value)
            return str(rolled_value)

        except Exception as err:
            span.record_exception(err)
            span.set_status(Status(StatusCode.ERROR, str(err)))
            log.error("Dice roll failed: %s", err)
            return f"Error occurred: {str(err)}", 500

def roll_dice_logic():
    number = randint(1, 6)
    if number == 1:
        raise ValueError("Critical failure! Dice landed on 1")
    return number
