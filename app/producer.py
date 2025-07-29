from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    key_serializer=lambda k: k.encode('utf-8'),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def enviar_venda(venda: dict):
    producer.send("sales", key=venda["produto"], value=venda)
    producer.flush()

def enviar_log(log: dict):
    producer.send("logs", key=log["tipo"], value=log)
    producer.flush()
