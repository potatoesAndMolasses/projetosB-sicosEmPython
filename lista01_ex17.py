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