from fastapi import FastAPI
from BancoDados import bd
from pydantic import BaseModel

app = FastAPI()


@app.get('/alimentos/')
def buscarTodosOsAlimentos():
    reposta = bd.getAlimentos()
    return {
        'dados': reposta,
        'statusCode': 200
    }

@app.get('/alimentos/{id}')
def buscarUmAlimento(id: int):
    return bd.getAlimento(id)

