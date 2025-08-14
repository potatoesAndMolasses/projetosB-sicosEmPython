# Conversor de Moeda
# Este script converte um valor em reais para dólares, euros e libras.
# As taxas de conversão são fictícias e devem ser atualizadas conforme necessário.
def dolar(valorReal):
    valorDolar = valorReal / 5.54
    print("Em dolares temos {:.2f}".format(valorDolar))

def euro(valorReal):
    valorEuro = valorReal / 6.42
    print("Em euros temos {:.2f}".format(valorEuro))

def libra(valorReal):
    valorLibra = valorReal / 7.36
    print("Em libras temos {:.2f}".format(valorLibra))

def main():
    valorReal = float(input("Digite um valor em real: "))
    dolar(valorReal)
    euro(valorReal)
    libra(valorReal)
if __name__=="__main__":
    main()