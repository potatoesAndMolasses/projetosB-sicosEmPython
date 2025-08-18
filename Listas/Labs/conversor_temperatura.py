# Conversor de Temperatura
# Este script converte uma temperatura em Celsius para Fahrenheit ou Kelvin.
# O usuário escolhe a unidade de conversão desejada.
# As fórmulas de conversão são:
# Fahrenheit = (Celsius * 9/5) + 32
# Kelvin = Celsius + 273.15
def conversor():
    temperaturaCelsius = int(input("Digite a temperatura em Celsius: "))
    escolha = input("Você deseja a temperatura em Fahrenheit ou Kelvin?")
    
    if escolha.lower() == "fahrenheit":
        resultado = (temperaturaCelsius * 9/5) + 32
        print("A temperatura em Fahrenheit é de: {:.2f}".format(resultado))
    elif escolha.lower() == "kelvin":
        resultado = (temperaturaCelsius + 273.15)
        print("A temperatura em Kelvin é de: {:.2f}".format(resultado))
    else:
        print("Unidade desconhecida.")
conversor()