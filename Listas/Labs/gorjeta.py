# Gorjeta e Divisão de Conta
# Este script calcula a gorjeta e divide a conta entre amigos.
def bill_split():
    friends = int(input("Digite a quantidade de amigos: "))
    amount = float(input("Digite o valor da conta: "))
    daCasa = amount * 1.2
    quantiaIndividual = daCasa / friends
    print("O total com os 20% foi {:.2f} e cada um deve pagar {:.2f}".format(daCasa, quantiaIndividual))

bill_split()