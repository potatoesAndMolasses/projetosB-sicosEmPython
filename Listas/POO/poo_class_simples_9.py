# Classe simples
# Crie uma classe Computador com atributos marca e ram.

class Computador:
    def __init__(self, marca, ram):
        self.marca = marca
        self.ram = ram
    
    def mostrar_informacoes(self):
        return f"Marca: {self.marca}, RAM: {self.ram}GB"
# Exemplo de uso
computador1 = Computador("Dell", 16)
computador2 = Computador("HP", 8)
print(computador1.mostrar_informacoes())
print(computador2.mostrar_informacoes())