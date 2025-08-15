# Classe simples
# Crie uma classe Curso com atributos nome e duracao.

class Curso:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def mostrar_informacoes(self):
        return f"Curso: {self.nome}, Duração: {self.duracao} horas"
# Exemplo de uso
curso1 = Curso("Python Básico", 40)
curso2 = Curso("Desenvolvimento Web", 60)
print(curso1.mostrar_informacoes())
print(curso2.mostrar_informacoes())