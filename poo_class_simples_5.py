# Classe simples
# Crie uma classe Funcionario com atributos nome e salario.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def mostrar_informacoes(self):
        return f"Nome: {self.nome}, Salário: {self.salario}"
    
# Exemplo de uso
funcionario1 = Funcionario("Carlos", 3000)
funcionario2 = Funcionario("Ana", 4500)
print(funcionario1.mostrar_informacoes())
print(funcionario2.mostrar_informacoes())