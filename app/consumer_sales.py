from kafka import KafkaConsumer
import json
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import SessionLocal
from app.models import Venda
from app.logger_config import get_logger
from sqlalchemy.orm import Session

logger = get_logger("vendas_consumer")

consumer = KafkaConsumer(
    'sales',
    group_id='grupo_vendas',
    bootstrap_servers='kafka:9092',
    enable_auto_commit=False,
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    key_deserializer=lambda k: k.decode('utf-8') if k else None
)

db: Session = SessionLocal()

for msg in consumer:
    try:
        data = msg.value
        venda = Venda(produto=data["produto"], valor=data["valor"], data=data["data"])
        db.add(venda)
        db.commit()
        logger.info(f"Venda salva: {data}")
        consumer.commit()
    except Exception as e:
        logger.error(f"Erro ao processar: {e}")
