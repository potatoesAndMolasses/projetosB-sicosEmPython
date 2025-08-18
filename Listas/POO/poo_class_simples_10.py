# Classe simples
# Crie uma classe ContaBancaria com atributo saldo.
# Adicione métodos depositar(valor) e sacar(valor),
# que atualizam o saldo. O método sacar deve verificar se há saldo suficiente.

class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado. Saldo atual: {self.saldo}")
    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saldo insuficiente para sacar {valor}. Saldo atual: {self.saldo}")
        else:
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Saldo atual: {self.saldo}")
# Exemplo de uso
conta = ContaBancaria(100)
conta.depositar(50)
conta.sacar(30)
conta.sacar(150)  # Tentativa de saque maior que o saldo
print(f"Saldo final: {conta.saldo}")