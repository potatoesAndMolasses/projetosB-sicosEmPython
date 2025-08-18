# Classe simples
# Crie uma classe Carro com atributos marca e modelo.

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacoes(self):
        return f"Carro: {self.marca} {self.modelo}"
    
# Exemplo de uso
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

print(carro1.mostrar_informacoes())
print(carro2.mostrar_informacoes())