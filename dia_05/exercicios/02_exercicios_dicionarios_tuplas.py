#%% Exercício 2
# Escreva um programa que solicite ao usuário frases. 
# Para parar de solicitar frases, ele pode apenas apertar o “enter”.
# Seu programa deve apresentar cada frase e quantas vezes ela foi repetida.

lista_frases = {}

while True:
    frase_inputada = input("Frase")
    
    if frase_inputada == "":
        break
    
    if frase_inputada not in lista_frases:
        lista_frases[frase_inputada] = 1
    else:
        lista_frases[frase_inputada] += 1

for frase in lista_frases:
    print(frase, "->", lista_frases[frase])