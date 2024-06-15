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

    def setAlimento(self, alimento: Alimento):
        chaves = self.dados.keys()
        for chave in chaves:
            if alimento.id == chave:
                return {"dados": "o id informado já existe dentro do banco", "statusCode": 400}
        self.dados[alimento.id]= alimento
        return  {"dados": alimento, "info": "alimento criado com sucesso", "statusCode": 200}

    def excluirAlimento(self, id: int):
        chaves = self.dados.keys()
        for chave in chaves:
            if id == chave:
                alimentoExcluido = self.dados[id]
                del self.dados[id]
                return {"Alimento Excluido": alimentoExcluido, "info": "alimento excluido com sucesso", "statusCode": 200}



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
