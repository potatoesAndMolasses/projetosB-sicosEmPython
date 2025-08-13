import math

def letraA(x):
    y = (1/4*(x**2))-3
    print("Na letra A o valor de y é {:.2f}".format(y))

def letraB(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Sem raízes reais.")
    else:
        y = -b + math.sqrt(delta) / 2*a
        print("Na letra B, com os valores de a {:.2f}, b {:.2f} e c {:.2f}. Encontramos y valendo {:.2f}".format(a, b, c, y))

def letraC(a, b, c):
    y = -2*(a/c) * math.cos(b) * math.sin(b)
    print("Na letra C, com os valores de a {:.2f}, b {:.2f} e c {:.2f}. Encontramos y valendo {:.2f}".format(a, b, c, y))

def main():
    x = int(input("Digite o valor de x: "))
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    letraA(x)
    letraB(a, b, c)
    letraC(a, b, c)
if __name__=="__main__":
    main()