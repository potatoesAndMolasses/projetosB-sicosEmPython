# Encontrando Vogais
# Este script conta a quantidade de vogais em uma frase digitada pelo usuário.
# As vogais consideradas são: a, e, i, o, u (tanto minúsculas quanto maiúsculas).
def contador():
    contador = 0
    frase = input("Digite uma frase: ")
    for letra in frase.lower():
        if letra in "aeiou":
            contador += 1
    print("A quantidade de vogais é {}".format(contador))
contador()