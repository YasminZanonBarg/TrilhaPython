#%% 1) Faça um programa que vende uma garrafa de água:
#   a. Se o cliente escolher água mineral natural, será cobrado R$1,50
#   b. Se o cliente escolher água mineral com gás, será cobrado R$2,50
texto = """
    Qual produto você deseja: 
        a) água mineral (digite o número 1)
        b) água com gás (digite o número 2)
"""

produto = input(texto)

conta = 0
if produto == "1":
    conta = 1.5
elif produto == "2":
    conta = 2.5
else:
    print("Produto inexistente")

print("Valor da conta é: R$", conta)

#%% 2) Altere o programa anterior para considerar a quantidade de garrafas de água
produto = """
    Qual produto você deseja: 
        a) água mineral (digite o número 1)
        b) água com gás (digite o número 2)
"""
produto = input(texto)

valor_item = 0
if produto == "1":
    valor_item = 1.5 
elif produto == "2":
    valor_item = 2.50

if valor_item == 0:
    print("Produto inexistente")
else:
    quantidade_garrafas = input("Quantas garrafas?")
    quantidade_garrafas = int(quantidade_garrafas)
    valor_total = valor_item * quantidade_garrafas
    print("Valor da conta é: R$", conta)

#%% 3) Faça o programa de uma sorveteria, onde o usuário pode escolher:
#   a. Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
#   b. Sabor do sorvete: morango, creme, chocolate
#   c. Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
#   Apresente o valor a ser pago

tipo_sorvete = int(input("Tipo desejado: casquinha (digite 1), cascão (digite 2), cestinha (digite 3)"))
sabor_sorvete = int(input("Sabor desejado: morango (digite 1), creme (digite 2), chocolate (digite 3)"))
cobertura_sorvete = int(input("Cobertura desejada: Caramelo (digite 1), morango (digite 2), chocolate (digite 3),  sem cobertura (digite 4)"))

if tipo_sorvete == 1:
    valor_tipo_sorvete = 1.0
elif tipo_sorvete == 2:
    valor_tipo_sorvete = 2.5
elif tipo_sorvete == 3:
    valor_tipo_sorvete = 4.0
else:
    print("Produto inexistente")

if cobertura_sorvete in (1, 2, 3):
    valor_cobertura_sorvete = 1.5
elif cobertura_sorvete == 4:
    valor_tipo_sorvete = 0.0
else:
    print("Produto inexistente")

valor_total = valor_tipo_sorvete + valor_tipo_sorvete
print("Valor total: R$", valor_total)