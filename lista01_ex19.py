# lista01_ex19.py
# Este script calcula o comprimento, a área e o volume de uma esfera com base no raio fornecido pelo usuário.
# As fórmulas utilizadas são:
# Comprimento = 2 * π * raio
# Área = π * raio²
# Volume = (4/3) * π * raio³
# O resultado é impresso com duas casas decimais.
import math

def contas(a):
    comprimento = 2 * math.pi * a
    area = math.pi * a**2
    volume = 4/3 * math.pi * a**3
    print("Com o raio {:.2f}, obtemos o comprimento {:.2f}, " \
    "a área {:.2f} e" \
    " o volume {:.2f}.".format(a, comprimento, area, volume))

def main():
    r = int(input("Digite um valor para o raio: "))
    contas(r)
if __name__=="__main__":
    main()