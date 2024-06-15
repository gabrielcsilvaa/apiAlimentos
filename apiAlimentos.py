#primeiro é from -- import
from fastapi import FastAPI
from BancoDados import bd

app = FastAPI()

@app.get('/alimentos/')
def buscarTodosAlimentos():
    reposta = bd.dados
    return {
        'dados': reposta,
        'status Code' : 200
    }
