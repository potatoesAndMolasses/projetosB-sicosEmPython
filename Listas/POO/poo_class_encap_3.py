# Encapsulamento
# Crie uma classe Produto com atributo privado preco.
# Crie método alterar_preco() com validação para valor positivo

class Produto():
    def __init__(self, preco_inicial=0):
        self.__preco = preco_inicial
    def alterar_preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
            print(f"Preço alterado para R${self.__preco:.2f}")
        else:
            print("O preço deve ser um valor positivo.")
# Exemplo de uso
produto = Produto(100)
produto.alterar_preco(150)
produto.alterar_preco(-50)