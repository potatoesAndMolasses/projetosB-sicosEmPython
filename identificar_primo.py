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