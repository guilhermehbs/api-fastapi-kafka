from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, DateTime

Base = declarative_base()

class Venda(Base):
    __tablename__ = "vendas"
    id = Column(Integer, primary_key=True)
    produto = Column(String)
    valor = Column(Numeric)
    data = Column(DateTime)

class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    mensagem = Column(String)
    data = Column(DateTime)
