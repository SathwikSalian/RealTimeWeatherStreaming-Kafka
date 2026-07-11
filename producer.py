# producer.py

from kafka import KafkaProducer
import json
import time
from datetime import datetime


from weather_api import get_weather
from config import BOOTSTRAP_SERVER, TOPIC_NAME, CITY


producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("Producer Started...\n")

while True:

    temperature = get_weather()

    message = {
        "city": CITY,
        "temperature": temperature,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    producer.send(TOPIC_NAME, value=message)

    producer.flush()

    print("Sent :", message)

    # Testing interval (30 seconds)
    time.sleep(10)

    # Change to 3600 later for every hour
