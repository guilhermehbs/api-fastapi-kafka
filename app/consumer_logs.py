from kafka import KafkaConsumer
import json
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import SessionLocal
from app.models import Log
from app.logger_config import get_logger

logger = get_logger("logs_consumer")

consumer = KafkaConsumer(
    'logs',
    group_id='grupo_logs',
    bootstrap_servers='kafka:9092',
    enable_auto_commit=False,
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    key_deserializer=lambda k: k.decode('utf-8') if k else None
)

db = SessionLocal()

for msg in consumer:
    try:
        data = msg.value
        log = Log(tipo=data["tipo"], mensagem=data["mensagem"], data=data["data"])
        db.add(log)
        db.commit()
        logger.info(f"Log salvo: {data}")
        consumer.commit()
    except Exception as e:
        logger.error(f"Erro ao processar log: {e}")
