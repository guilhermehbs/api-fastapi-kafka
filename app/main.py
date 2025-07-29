from fastapi import FastAPI
from app.schemas import VendaSchema, LogSchema
from app.producer import enviar_venda, enviar_log

app = FastAPI()

@app.post("/venda")
def post_venda(venda: VendaSchema):
    enviar_venda(venda.dict())
    return {"mensagem": "Venda publicada"}

@app.post("/log")
def post_log(log: LogSchema):
    enviar_log(log.dict())
    return {"mensagem": "Log enviado"}
