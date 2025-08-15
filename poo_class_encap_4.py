# Encapsulamento
# Crie uma classe Livro com atributo privado paginas.
# Crie método adicionar_paginas(n) para incrementar páginas.

class Livro():
    def __init__(self, paginas_iniciais=0):
        self.__paginas = paginas_iniciais

    def adicionar_paginas(self, n):
        if n > 0:
            self.__paginas += n
            print(f"{n} páginas adicionadas. Total de páginas: {self.__paginas}")
        else:
            print("Número de páginas a adicionar deve ser positivo.")

    def ver_paginas(self):
        return self.__paginas
# Exemplo de uso
livro = Livro()
livro.adicionar_paginas(50)