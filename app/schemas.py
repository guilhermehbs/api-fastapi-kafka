from pydantic import BaseModel
from datetime import datetime

class VendaSchema(BaseModel):
    produto: str
    valor: float
    data: datetime

class LogSchema(BaseModel):
    tipo: str
    mensagem: str
    data: datetime
