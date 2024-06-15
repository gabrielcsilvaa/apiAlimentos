from pydantic import BaseModel

class Alimento:

    def __init__(self, id:int, nome:str, preco:float, disponibilidade:bool, quantidade:int, imagem: str):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.disponibilidade = bool
        self.quantidade = quantidade
        self.imagem = imagem

alimento1 = Alimento(1, 'uva', 10.50, True, 10, '')

print (alimento1.quantidade)




