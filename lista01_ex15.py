def nome(nan):
    print("Boa tarde, {}! Como você está?".format(nan))

def main():
    nan = input("Digite seu primeiro nome: ")
    nome(nan)
if __name__=="__main__":
    main()