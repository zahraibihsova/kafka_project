from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers=["52.205.188.82:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    data = {"sensor_id": random.randint(1,5), "temperature": round(random.uniform(20,30),2)}
    producer.send("sensor-data", value=data)
    print("Sent:", data)
    time.sleep(2)
