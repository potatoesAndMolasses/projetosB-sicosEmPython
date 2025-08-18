# Classe simples
# Crie uma classe Aluno com atributos nome e nota. 
# Adicione um método aprovado() que retorna True se a nota for ≥ 6.0 e False caso contrário.

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def aprovado(self):
        return self.nota>= 6.0
    
# Exemplo de uso
aluno1 = Aluno("João", 7.5)
aluno2 = Aluno("Maria", 5.0)

print(f"{aluno1.nome} aprovado: {aluno1.aprovado()}")
print(f"{aluno2.nome} aprovado: {aluno2.aprovado()}")