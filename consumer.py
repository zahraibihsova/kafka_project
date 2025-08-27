from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "sensor-data",
    bootstrap_servers=["52.205.188.82:9092"],  
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

try:
    for msg in consumer:
        print("Received:", msg.value)
except KeyboardInterrupt:
    print("\nStopping consumer...")
finally:
    consumer.close()
    print("Consumer closed.")
