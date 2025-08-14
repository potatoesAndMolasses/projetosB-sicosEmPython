class Fila():
    def __init__(self):
        self.itens = []

    def enqueue(self, valor): # enfileirar
        self.itens.append(valor)

    def dequeue(self): # desenfileirar
        if not self.esta_vazia():
            self.itens.pop(0)

    def view(self): # visualizar
        return self.itens

    def esta_vazia(self):
        return len(self.itens) == 0
f = Fila()