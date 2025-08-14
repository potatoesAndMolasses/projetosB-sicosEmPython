# Identificador de Números Primos
# Este script verifica se um número é primo.
# Um número é considerado primo se for maior que 1 e divisível apenas por 1 e por ele mesmo.
# Exemplo: 2, 3, 5, 7
# Números como 4, 6, 8, 9 não são primos, pois têm mais divisores.
def primo():
    valor = int(input("Digite um valor: "))
    contador = 0

    for i in range(1, valor + 1):
        if valor % i == 0:
            contador += 1
    
    if contador == 2:
        print("Temos um primo.")
    else:
        print("Não é primo.")
primo()