# consumer.py

from kafka import KafkaConsumer
import json

from config import BOOTSTRAP_SERVER, TOPIC_NAME


consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=BOOTSTRAP_SERVER,
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Waiting for messages...\n")

for message in consumer:

    data = message.value

    print("----------------------------")
    print("City        :", data["city"])
    print("Temperature :", data["temperature"], "°C")
    print("Time        :", data["time"])
    print("----------------------------")