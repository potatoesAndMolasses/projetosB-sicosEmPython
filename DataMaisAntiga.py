def MaisAntiga(data_1, data_2):
    """
    Recebe duas datas no formato DDMMAAAA (sem barras) como inteiros
    e retorna a mais antiga no formato DD/MM/AAAA.
    """
    dia1 = data_1 // 1000000
    mes1 = (data_1 // 10000) % 100
    ano1 = data_1 % 10000

    dia2 = data_2 // 1000000
    mes2 = (data_2 // 10000) % 100
    ano2 = data_2 % 10000

    if ano1 < ano2:
        return f"{dia1:02d}/{mes1:02d}/{ano1:04d}"
    elif ano1 > ano2:
        return f"{dia2:02d}/{mes2:02d}/{ano2:04d}"
    else:
        if mes1 < mes2:
            return f"{dia1:02d}/{mes1:02d}/{ano1:04d}"
        elif mes1 > mes2:
            return f"{dia2:02d}/{mes2:02d}/{ano2:04d}"
        else:
            if dia1 <= dia2:
                return f"{dia1:02d}/{mes1:02d}/{ano1:04d}"
            else:
                return f"{dia2:02d}/{mes2:02d}/{ano2:04d}"

# Exemplo de uso:
data_1 = int(input("Digite a primeira data (formato DDMMAAAA): "))
data_2 = int(input("Digite a segunda data (formato DDMMAAAA): "))

print("Data mais antiga:", MaisAntiga(data_1, data_2))

