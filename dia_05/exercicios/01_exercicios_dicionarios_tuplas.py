#%% Exercício 1
# Solicite ao usuário o nome de uma fruta e exiba o preço correspondente:
# Maçã: R$1,50
# Banana: R$2,75
# Uva: R$1,90
# Pera: R$1,25
# Laranja: R$0,65
# Limão: R$1,25
# Goiaba: R$2,15
# Abacaxi: R$3,20
# Jaca: R$5,80

valores_frutas = {
    "Maçã": 1.50,
    "Banana": 2.75,
    "Uva": 1.90,
    "Pera": 1.25,
    "Laranja": 0.65,
    "Limão": 1.25,
    "Goiaba": 2.15,
    "Abacaxi": 3.20,
    "Jaca": 5.80
}

fruta_desejada = input("Qual fruta você deseja saber o preço?")

if fruta_desejada in valores_frutas:
    print(valores_frutas[fruta_desejada])
else:
    print("Entre com um valor válido!")


# Esse exemplo simples é um insight valioso, pois poderiamos estar 
# utilizando uma estrutura com muitos ifs que seria honeroso 
# e de ruim manutenção - Evite utilizar muito IF
# Dessa forma podemos ter mais performance utilizando a estrutura do Python