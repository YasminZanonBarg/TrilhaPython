# %% for = percorre os elementos de um objeto
nome = "Yasmin Zanon Barg"

for letra in nome:
    print(letra)


# %% Imprimir a tabuada do 2 até 100
numero = 2
max_numero = 100

for multiplicador in range(1, max_numero + 1):
    print(numero, "x", multiplicador, "=", numero * multiplicador)


#%% Quais são os números divisiveis por 4 no intervalo de 4 até 100
dividendo = 4
max_divisor = 100

for divisor in range(1, max_divisor + 1):
    if divisor % dividendo == 0:
        print(divisor)
