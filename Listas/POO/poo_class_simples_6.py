# Classe simples
# Crie uma classe Pessoa com atributos nome e altura.

class Pessoa:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura
    
    def mostrar_informacoes(self):
        return f"Nome: {self.nome}, Altura: {self.altura}"
# Exemplo de uso
pessoa1 = Pessoa("Carlos", 1.75)
pessoa2 = Pessoa("Ana", 1.65)
print(pessoa1.mostrar_informacoes())
print(pessoa2.mostrar_informacoes())