class Veiculo:
    def __init__(self):
        self.tipo = "Veículo genérico"

    def obterTipo(self):
        return self.tipo
    
class Carro(Veiculo):
    def __init__(self):
        super().__init__()
        self.tipo = "Carro"
    
v = Veiculo()
c = Carro()

print(v.obterTipo())  # Veículo genérico
print(c.obterTipo())  # Carro
