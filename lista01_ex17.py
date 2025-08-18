# lista01_ex17.py
# Este script calcula uma fórmula matemática baseada em um valor inteiro fornecido pelo usuário.
# A fórmula é: 9.87 * sin(2 * b) - 7.53 * cos(b) - 1.5 * sin(b)
# Onde b é calculado como (2 * π * (a - 81)) / 365.
# O resultado é impresso com duas casas decimais.
import math

def calculaN(a):
    b = (2 * math.pi * (a - 81)) / 365
    resultado = 9.87 * math.sin(2 * b) - 7.53 * math.cos(b) - 1.5 * math.sin(b)
    print("O resultado da formula é: {:.2f}".format(b))
    print("A trigonometria, vale {:.2f}".format(resultado))

def main():
    n = int(input("Digite um valor inteiro: "))
    calculaN(n)
if __name__=="__main__":
    main()