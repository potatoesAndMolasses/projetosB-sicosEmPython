# Encapsulamento
# Crie uma classe Conta que tenha um atributo privado saldo e métodos para depositar e sacar.
# Garantindo que não seja possível sacar mais que o saldo.

class Conta():
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.__saldo:.2f}")
        else:
            print("Valor de depósito deve ser positivo.")
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.__saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")
# Exemplo de uso 
conta = Conta()
conta.depositar(50)
conta.sacar(30)
conta.sacar(150)