"""
Faça um programa que dado o número do mês, retorne o nome daquele mês. Caso
o mês não exista seu programa deve retornar um aviso ao usuário.
"""


# Lista com os nomes dos meses (índice 0 = janeiro, índice 11 = dezembro)
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Entrada do usuário
numero = int(input("Digite o número do mês (1 a 12): "))

# Verificação e saída
if 1 <= numero <= 12:
    nome_mes = meses[numero - 1]  # Ajusta o índice para a lista (começa do 0)
    print(f"O mês correspondente é: {nome_mes}")
else:
    print("Mês inválido. Por favor, digite um número entre 1 e 12.")

