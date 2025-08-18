
class Animal:
    def falar(self):
        return "Som genérico"

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

animais = [Cachorro(), Gato()]
for animal in animais:
    print(animal.falar())