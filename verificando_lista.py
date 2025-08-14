# Crie uma função que receba uma lista de números e retorne apenas os pares.
def pares(lista):
    return [x for x in lista if x % 2 == 0]

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = pares(list)
print(resultado)

