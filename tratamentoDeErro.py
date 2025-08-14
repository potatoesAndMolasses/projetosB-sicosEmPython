# tratamentoDeErro.py
# Este script demonstra o tratamento de erros em Python.
# Ele tenta dividir um número inteiro por 100 e captura erros comuns como
# ZeroDivisionError e ValueError, imprimindo mensagens apropriadas para o usuário.
try:
    valor = int(input("Digite um numero inteiro:"))
    resp = valor / 100
    print(f"O resultado da divisão por cem foi: {resp}")
except ZeroDivisionError:
    print("Nao podemos dividir por zero.")
except ValueError:
    print("O valor digitado deve ser inteiro.")