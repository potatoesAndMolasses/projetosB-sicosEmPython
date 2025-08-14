def media():
    p1 = int(input("Digite o valor da primeira prova: "))
    p2 = int(input("Digite o valor da segunda prova: "))
    p3 = int(input("Digite o valor da terceira prova: "))
    
    m = (p1 + p2 + p3) / 3

    if m >= 7:
        print("Aprovado com média {:.2f}".format(m))
    elif (m > 5 and m < 7):
        print("Recuperação com média {:.2f}".format(m))
    else:
        print("Reprovado, com média {:.2f}".format(m))
media()