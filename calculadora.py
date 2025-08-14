class operacoes( ):
    
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    
    def soma(self):
        return self.valor1 + self.valor2
    
    def subtracao(self):
        return self.valor1 - self.valor2
    
    def multiplicacao(self):
        return self.valor1 * self.valor2
    
    def divisao(self):
        if self.valor2 == 0:
            return None
        else:
            return self.valor1 / self.valor2

v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))

op = operacoes(v1, v2)

print("Soma:", op.soma())
print("Subtração:", op.subtracao())
print("Multiplicação:", op.multiplicacao())

resultadoDiv = op.divisao()
if resultadoDiv is None:
    print("Não podemos dividir por zreo.")
else:
    print("Divisão: ", op.divisao())