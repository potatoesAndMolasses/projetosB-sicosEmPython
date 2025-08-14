# Crie uma função que receba um número e retorne o fatorial dele.
def fatorial(numero):
    if numero < 0:
        return None
    
    resp = 1
    
    while numero > 1:
        resp *= numero
        numero -= 1
    
    return resp

resultado = fatorial(5)
print(resultado)