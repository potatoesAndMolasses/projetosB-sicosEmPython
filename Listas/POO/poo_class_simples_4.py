# Classe simples
# Crie uma classe Produto com atributos nome e preco.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def mostrar_informacoes(self):
        print(f"Produto: {self.nome}, Preço: R${self.preco:.2f}")
# Exemplo de uso
produto1 = Produto("Notebook", 2500.00)
produto1.mostrar_informacoes()