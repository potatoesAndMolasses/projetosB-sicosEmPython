try:
    valor = int(input("Digite um numero inteiro:"))
    resp = valor / 100
    print(f"O resultado da divisão por cem foi: {resp}")
except ZeroDivisionError:
    print("Nao podemos dividir por zero.")
except ValueError:
    print("O valor digitado deve ser inteiro.")