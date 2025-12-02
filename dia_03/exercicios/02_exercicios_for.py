#%% 2) Faça um programa que receba 4 alturas usando um laço de repetição e realize a soma dessas alturas.
valor_total_altura = 0

for altura in range(1, 5):
    valor_altura = float(input(f"Insira o valor da altura {altura}"))
    valor_total_altura = valor_total_altura + valor_altura
    altura -= 1

print("Valor total alturas:", valor_total_altura)


#%% 3) Faça um programa que receba uma quantidade indefinida de valores correspondentes a “saldo em conta”, mas quando o usuário apertar “enter” sem digitar valor algum, o programa para de receber valores, e exibe a soma de todos os valores digitados anteriormente.
saldo = 0
total = 0

while saldo != "":
    saldo = input("Informe o valor recebido")

    if saldo != "":
        total = total + float(saldo)

print(f"Saldo atualizado = {total}")