# Encapsulamento
# Crie uma classe ContaBancaria com método ver_saldo() que retorna saldo privado.
# Crie método transferir(valor, outra_conta) que subtrai do saldo da conta atual e adiciona à outra.

class ContaBancaria():
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial
    
    def ver_saldo(self):
        return self.__saldo

    def transferir(self, valor, outra_conta):
        if 0 <= valor <= self.__saldo:
            self.__saldo -= valor
            outra_conta.__saldo += valor
            print(f"Transferência de R${valor:.2f} realizada. Saldo atual: R${self.__saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido para transferência.")
# Exemplo de uso
conta1 = ContaBancaria(100)
conta2 = ContaBancaria(50)
print(f"Saldo conta1: R${conta1.ver_saldo():.2f}")
print(f"Saldo conta2: R${conta2.ver_saldo():.2f}")
conta1.transferir(30, conta2)
print(f"Saldo conta1: R${conta1.ver_saldo():.2f}")
print(f"Saldo conta2: R${conta2.ver_saldo():.2f}")
conta1.transferir(80, conta2)  # Tentativa de transferência inválida