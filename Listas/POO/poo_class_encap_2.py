# Encapsulamento
# Crie uma classe Aluno com atributo privado nota.
# Crie método definir_nota() que valida se a nota é de 0 a 10.

class Aluno():
    def __init__(self, nota_inicial=0):
        self.__nota_inicial = nota_inicial
    def definir_nota(self, nota):
        if 0<= nota <= 10:
            self.__nota_inicial = nota
            print(f"Nota definida como {self.__nota_inicial:.1f}")
        else:
            print("Nota inválida. Deve ser entre 0 e 10.")
# Exemplo de uso
aluno = Aluno()
aluno.definir_nota(8.5)
aluno.definir_nota(11)  # Tentativa de definir nota inválida
aluno.definir_nota(7.0)  # Definindo uma nota válida
aluno.definir_nota(-1)  # Tentativa de definir nota inválida

