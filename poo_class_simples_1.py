# Classe simples
# Crie uma classe Aluno com atributos nome e idade.

class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

# Exemplo de uso
aluno1 = Aluno("João", 20)
aluno1.mostrar_informacoes()
aluno2 = Aluno("Maria", 22)
aluno2.mostrar_informacoes()