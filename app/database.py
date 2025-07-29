from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time

DATABASE_URL = "postgresql://postgres:postgres@postgres:5432/sistema"

while True:
    try:
        engine = create_engine(DATABASE_URL)
        SessionLocal = sessionmaker(bind=engine)
        break
    except Exception as e:
        print("Esperando PostgreSQL", e)
        time.sleep(2)
