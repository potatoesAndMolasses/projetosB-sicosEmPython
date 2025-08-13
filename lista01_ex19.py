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