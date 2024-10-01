import json
from kafka import KafkaProducer


def send_message_to_kafka(topic, message):
    print('AAAA')
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    producer.send(topic, message)
    producer.flush()
