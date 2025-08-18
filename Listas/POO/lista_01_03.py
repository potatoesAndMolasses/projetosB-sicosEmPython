"""
Escreva em uma classe NumeroComplexo, que representa um número complexo. A classe deve fornecer as seguintes operações:
a) Construtor com valores das partes inteira e fracionária;
b) Métodos getter/setter para os atributos da parte inteira e parte imaginária;
c) Método somar, que recebe outro número complexo e o adiciona ao número complexo que recebeu a mensagem. 
(a+bi)+(c+di) = (a+c)+(b+d)i;
d) Método subtrair, que recebe outro número complexo e o subtrai do número complexo que recebeu a mensagem. 
(a+bi)−(c+di) = (a−c)+(b−d)i;
e) Método multiplicar, que recebe outro número complexo e o multiplica ao complexo que recebeu a mensagem:
(a+bi) * (c+di) = (ac−bd)+(ad+bc)i;
f) Método dividir, que recebe outro número complexo e o divide ao complexo que recebeu a mensagem: 
(a+bi) / (c+di) = (ac+bd)/(c2 +d2) + (bc-ad)/(c2 + d2)i;
g) Um método de comparação semântica dos números complexos;
h) Um método que gere e retorne a representação string do número complexo;
i) Um método que retorne o módulo do número complexo.
"""

class NumeroComplexo:
    def __init__(self, parte_real: float = 0.0, parte_imaginaria: float = 0.0):
        """"Incializa o número complexo com parte real (foat) e parte imaginária (float)"""
        self.parte_real = parte_real
        self.parte_imaginaria = parte_imaginaria
    
    def get_parte_real(self) -> float:
        """Retorna a parte real do número complexo."""
        return self.parte_real
    def set_parte_real(self, parte_real: float) -> None:
        """Define a parte real do número complexo."""
        self.parte_real = parte_real

    def get_parte_imaginaria(self) -> float:
        """Retorna a parte imaginária do número complexo."""
        return self.parte_imaginaria
    def set_parte_imaginaria(self, parte_imaginaria: float) -> None:
        """Define a parte imaginária do número complexo."""
        self.parte_imaginaria = parte_imaginaria
    
    def somar(self, outro: 'NumeroComplexo') -> 'NumeroComplexo':
        """"Somamos a parte real e parte imaginária de dois números complexos."""
        return NumeroComplexo(
            self.parte_real + outro.parte_real,
            self.parte_imaginaria + outro.parte_imaginaria
        )
    
    def subtrair(self, outro: 'NumeroComplexo') -> 'NumeroComplexo':
        """Subtraímos a parte real e parte imaginária de dois números complexos."""
        return NumeroComplexo(
            self.parte_real - outro.parte_real,
            self.parte_imaginaria - outro.parte_imaginaria
        )
    
    def multiplicar(self, outro: 'NumeroComplexo') -> 'NumeroComplexo':
        """Multiplicamos dois números complexos."""
        a, b = self.parte_real, self.parte_imaginaria
        c, d = outro.parte_real, outro.parte_imaginaria
        return NumeroComplexo(
            a * c - b * d,
            a * d + b * c
        )
    
    def dividir(self, outro: 'NumeroComplexo') -> 'NumeroComplexo':
        """Dividimos dois números complexos."""
        a, b = self.parte_real, self.parte_imaginaria
        c, d = outro.parte_real, outro.parte_imaginaria
        divisor = c ** 2 + d ** 2
        return NumeroComplexo(
            (a * c + b * d) / divisor,
            (b * c - a * d) / divisor
        )
    
    def comparar(self, outro: 'NumeroComplexo') -> bool:
        """Compara dois números complexos."""
        return (self.parte_real == outro.parte_real and
                self.parte_imaginaria == outro.parte_imaginaria)
    
    def __str__(self) -> str:
        """Representa o número complexo como uma string."""
        return f"{self.parte_real} + {self.parte_imaginaria}i"
    
    def modulo(self) -> float:
        """Calcula o módulo do número complexo."""
        return (self.parte_real ** 2 + self.parte_imaginaria ** 2) ** 0.5
    