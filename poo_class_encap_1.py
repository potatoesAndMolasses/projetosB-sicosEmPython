# Encapsulamento
# Crie uma classe Funcionario com atributo privado salario.
# Crie métodos aumentar_salario() e consultar_salario().

class Funcionario:
    def __init__(self, salario):
        self.__salario = salario # atributo privado
    
    def auementar_salario(self, percentual):
        if percentual > 0:
            self.__salario += self.__salario * (percentual / 100)
        else:
            raise ValueError("Percentual deve ser positivo")
    
    def consultar_salario(self):
        return self.__salario

# Exemplo de uso
funcionario = Funcionario(3000)
print(f"Salário inicial: R${funcionario.consultar_salario():.2f}")
funcionario.auementar_salario(10)
print(f"Salário após aumento: R${funcionario.consultar_salario():.2f}")
try:
    funcionario.auementar_salario(-5)  # Tentativa de aumento inválido
except ValueError as e:
    print(f"Erro: {e}")