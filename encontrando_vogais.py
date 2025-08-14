def contador():
    contador = 0
    frase = input("Digite uma frase: ")
    for letra in frase.lower():
        if letra in "aeiou":
            contador += 1
    print("A quantidade de vogais é {}".format(contador))
contador()