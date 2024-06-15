from pydantic import BaseModel
from main import Alimento


class BancoDados:
    def __init__(self, objDados = {}):
        self.dados = objDados

    #add novo um novo alimento

    def addAlimento(self, alimento: Alimento):
        self.dados[alimento.id] = alimento


bd = BancoDados()

alimento2= Alimento(1, 'uva', 10.50, True, 10, '')

bd.addAlimento(alimento2)

print(bd.dados[1].nome)