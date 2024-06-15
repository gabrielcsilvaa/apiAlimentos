from pydantic import BaseModel
from Alimentos import Alimento, alimento1

class BancoDados:
    def __init__(self, objetoDados={}):
        self.dados = objetoDados

    #adicionar um novo alimento
    def adicionarAlimento(self, alimento: Alimento):
        self.dados[alimento.id] = alimento

    def getAlimentos(self):
        return self.dados

    def getAlimento(self, idAlimento):

        chaves = self.dados.keys()
        for chave in chaves:
            print(chave)
            if idAlimento == chave:
                return {"dados": self.dados[idAlimento], "statusCode": 200}

        return {"dados": "o id informado não existe no banco", "statusCode": 404}

    def setAlimentos(self, alimento: Alimento):
        chaves = self.dados.keys()
        for chaves in chaves:
            if alimento.id == chave:
                return {"dados": "o id informado ja existe dentro do banco": "statusCode": 400}


bd = BancoDados()

alimento2 = Alimento(1, 'teste', 10.50, True, 10, '')

bd.adicionarAlimento(alimento2)

idAlimento=1
chaves = bd.dados.keys()
for chave in chaves:
    print(chave)
    if idAlimento == chave:
        print ({"dados": bd.dados[idAlimento], "statusCode": 200})

print({"dados": "o id informado não existe no banco", "statusCode": 404})
