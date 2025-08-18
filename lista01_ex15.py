# lista01_ex15.py
# Este script solicita o primeiro nome do usuário e imprime uma mensagem personalizada.
def nome(nan):
    print("Boa tarde, {}! Como você está?".format(nan))

def main():
    nan = input("Digite seu primeiro nome: ")
    nome(nan)
if __name__=="__main__":
    main()