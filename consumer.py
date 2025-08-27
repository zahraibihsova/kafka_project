from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "sensor-data",
    bootstrap_servers=["52.205.188.82:9092:9092"],
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

for msg in consumer:
    print("Received:", msg.value)
