# Crie uma função contar_vogais que conte quantas vogais existem em uma string.
def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in palavra if letra in vogais)
print(contar_vogais("agua"))