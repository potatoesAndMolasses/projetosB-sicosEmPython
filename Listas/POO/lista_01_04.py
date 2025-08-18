"""
Escreva uma classe que represente uma reta (y=ax+b).
Forneça os seguintes membros de classe:
a) Construtores que criem uma reta a partir de:
i) Dois valores, representando o coeficiente angular e o coeficiente linear da reta;
ii) Dois pontos;
b) Métodos de acesso para o coeficiente angular e para o coeficiente linear da reta;
c) Um método que verifique se um ponto dado pertence a reta;
d) Um método que gere e retorne a representação String da reta;
e) Um método que dada uma outra reta, retorne o ponto d
"""

class Reta:
    def __init__(self, a=None, b=None, p1=None, p2=None):
        if a is not None and b is not None:
            self.a = a
            self.b = b
        elif p1 is not None and p2 is not None:
            x1, y1 = p1
            x2, y2 = p2
            if x2 != x1:
                self.a = (y2 - y1) / (x2 - x1)
                self.b = y1 - self.a * x1
            else:
                self.a = None  # reta vertical
                self.b = x1    # x = constante
        else:
            raise ValueError("Parâmetros inválidos para construção da reta.")
    
    def get_a(self) -> float:
        return self.a

    def set_a(self, a: float) -> None:
        self.a = a

    def get_b(self) -> float:
        return self.b

    def set_b(self, b: float) -> None:
        self.b = b

    def pertence(self, ponto: tuple) -> bool:
        x, y = ponto
        if self.a is None:
            return x == self.b  # reta vertical (x = b)
        return y == self.a * x + self.b

    def __str__(self) -> str:
        if self.a is None:
            return f"x = {self.b}"  # reta vertical
        return f"y = {self.a}x + {self.b}"

    def intersecao(self, outra: 'Reta') -> tuple:
        # Retas paralelas (iguais ou diferentes)
        if self.a == outra.a:
            return None

        # Se a reta atual é vertical: x = self.b
        if self.a is None:
            x = self.b
            y = outra.a * x + outra.b
            return (x, y)

        # Se a outra reta é vertical: x = outra.b
        if outra.a is None:
            x = outra.b
            y = self.a * x + self.b
            return (x, y)

        # Ambas são inclinadas (não verticais)
        x = (outra.b - self.b) / (self.a - outra.a)
        y = self.a * x + self.b
        return (x, y)
