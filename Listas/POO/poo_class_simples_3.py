# Classe simples
# Crie uma classe Livro com atributos titulo e autor.
class Livro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_informacoes(self):
        return f"{self.titulo} por {self.autor}"

# Exemplo de uso
livro1 = Livro("1984", "George Orwell")
livro2 = Livro("Dom Casmurro", "Machado de Assis")
print(livro1.mostrar_informacoes())
print(livro2.mostrar_informacoes())