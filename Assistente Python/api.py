from fastapi import FastAPI
from arduino import enviar

app = FastAPI(title="Assistente API Python")

@app.post("/executar")
def executar(comando: str):
    print("Comando recebido do Spring:", comando)

    resposta = enviar(comando)

    return {
        "status": "ok",
        "comando": comando,
        "resposta_arduino": resposta
    }
