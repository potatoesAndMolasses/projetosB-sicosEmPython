import random

def valorAleatorio():
    valor = random.randint(1, 100)
    tentativa = int(input("Tente adivinhar o valor: "))
    
    while (tentativa != valor):
        if valor > tentativa:
            print("O valor é maior")
            tentativa = int(input("Tente adivinhar o valor: "))
        else:
            print ("O valor é menor")
            tentativa = int(input("Tente adivinhar o valor: "))
valorAleatorio()