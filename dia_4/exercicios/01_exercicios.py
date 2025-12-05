# Escreva um programa que receba uma lista de números do usuário e 
# conte quantas vezes um número específico aparece na lista. 
# Solicite ao usuário um número e exiba a contagem.

lista = [1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9]

numero = int(input("Entre com um número:"))

contador = 0
for elemento in lista:
    if elemento == numero:
        contador += 1


print("Quantidade de", numero, ":", contador)