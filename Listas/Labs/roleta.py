# roleta.py
# Este script simula um jogo de roleta onde o usuário tenta adivinhar um valor
# aleatório entre 1 e 100. O usuário recebe dicas se o valor é maior ou menor
# do que o palpite dado. O jogo continua até que o usuário adivinhe o valor correto.
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