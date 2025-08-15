# Classe simples
# Crie uma classe Animal com atributos especie e idade.

class Animal:
    def __init__(self, especie, idade):
        self.especie= especie
        self.idade = idade

    def mostrar_informacoes(self):
        return f"Espécie: {self.especie}, Idade: {self.idade}"
    
# Exemplo de uso
animal1 = Animal("Cachorro", 5)
animal2 = Animal("Gato", 3)
print(animal1.mostrar_informacoes())
print(animal2.mostrar_informacoes())