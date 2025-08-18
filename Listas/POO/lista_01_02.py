"""
Escreva uma classe Ponto2D que represente um ponto no plano cartesiano. Além dos atributos por você identificados, a classe
deve oferecer os seguintes membros:
a) Construtores que permitam a inicialização do ponto:
i) Por default (sem parâmetros) na origem do espaço 2D;
ii) Num local indicado por dois parâmetros do tipo double (indicando o valor de abcissa e ordenada do ponto que está
sendo criado);
iii) Em um local indicado por outro ponto.
b) Métodos de acesso (getter/setter) dos atributos do ponto;
c) Métodos de movimentação do ponto com os mesmos parâmetros indicados para os construtores;
d) Método de comparação do ponto;
e) Método de representação do objeto como String;
f) Método que permita calcular a distância do ponto que recebe a mensagem, para outro ponto;
g) Método que permita a criação de um novo ponto no mesmo local do ponto que recebeu a mensagem (clone);
"""


class Ponto2D:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        """Inicializa o ponto com coordendas (x, y)."""
        self.x = x
        self.y = y
    
    def get_x(self) -> float:
        """Retorna a coordenada x do ponto."""
        return self.x
    def set_x(self, x: float) -> None:
        """Define a coordenada x do ponto."""
        self.x = x

    def get_y(self) -> float:
        """Retorna a coordenada y do ponto."""
        return self.y
    def set_y(self, y: float) -> None:
        """Define a coordenada y do ponto."""
        self.y = y  
    
    def mover(self, x: float, y: float) -> None:
        """Move o ponto para as novas coordenadas (x, y)."""
        self.x = x
        self.y = y
    
    def comparar(self, outro: 'Ponto2D') -> bool:
        """Compara este ponto com outro ponto."""
        return self.x == outro.x and self.y == outro.y
    
    def __str__(self) -> str:
        """Representa o ponto como uma string."""
        return f"Ponto2D({self.x}, {self.y})"
    
    def distancia(self, outro: 'Ponto2D') -> float:
        """Calcula a distância entre este ponto e outro ponto."""
        return ((self.x - outro.x) ** 2 + (self.y - outro.y) ** 2) ** 0.5
    
    def clone(self) -> 'Ponto2D':
        """Cria um novo ponto com as mesmas coordenadas deste ponto."""
        return Ponto2D(self.x, self.y)