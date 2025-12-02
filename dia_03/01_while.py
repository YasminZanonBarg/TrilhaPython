#%% Imprimir a tabuada do 2 até 100
numero = 2
multiplicador = 1

# While = Enquanto a condição for verdadeira, continua executando o laço
while multiplicador <= 100:
    print(numero, "*", multiplicador, "=", numero * multiplicador)
    multiplicador += 1 # multiplicador = multiplicador + 1

print("Finalizou!")


#%% Quais são os números divisiveis por 4 no intervalo de 4 até 100
dividendo = 4
divisor = 4

while divisor <= 100:
    if divisor % dividendo == 0:
        print(divisor)
    divisor += 1

print("Finalizou!")