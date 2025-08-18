# Crie uma função que receba duas listas e retorne uma nova lista com os elementos das duas (sem duplicatas).
def unir_listas(lista_1, lista_2):
    return list(set(lista_1 + lista_2))

print(unir_listas([1, 2, 3], [3, 4, 5]))