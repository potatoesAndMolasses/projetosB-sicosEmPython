"""
Escreva em uma classe Contador, que encapsule um valor usado para contagem de itens ou eventos. A classe deve oferecer métodos
que devem:
a) Zerar;
b) Incrementar;
c) Retornar o valor do contador.
"""
class Contador:
    
    def __init__(self):
        self.valor = 0

    def zerar(self) -> None:
        """Zera o contador."""
        self.valor = 0
    
    def incrementar(self) -> None:
        """Incrementa o contador em 1."""
        self.valor += 1

    def obter_valor(self) -> int:
        """Retorna o valor atual do contador."""
        return self.valor