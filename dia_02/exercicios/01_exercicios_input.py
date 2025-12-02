# %% | Exercício 1
# Faça um programa que dê bom dia;
print("Bom dia!")

# %% | Exercício 2
# Faça um programa que de bom dia, pergunta o nome da pessoa e responde que é um prazer conhecer ela, citando o nome da pessoa.
print("Bom dia!")

nome = input("Qual é o seu nome? ")

print("É um prazer em te conhecer", nome)

# %% | Exercício 3
#Crie uma história simples. Adicione essa história em um programa. A cada parágrafo, a história deve aguardar o usuário apertar “enter” para dar continuidade.
p1 = "Descubra minha lista de compras (De enter para ler o restante)"
p2 = "1. cream cheese (De enter para ler o restante)"
p3 = "2. ovos (De enter para ler o restante)"
p4 = "3. creme de leite (De enter para ler o restante)"
p5 = "4. frutas vermelhas"

input(p1)
input(p2)
input(p3)
input(p4)
input(p5)


# %% | Exercício 4
# Faça um programa que receba um número inteiro e calcule sua raiz quadrada e exiba o resultado.
numero = input("Quero saber a raiz quadrada do número:")
numero = int(numero)

raiz_quadrada = numero ** 0.5
raiz_quadrada = round(raiz_quadrada, 4)

print("A raiz quadrada de", numero, "é:", raiz_quadrada)


# %% | Exercício 5
# Faça um programa que exiba o dobro de um número inserido pelo usuário.
numero = input("Quero saber o dobro do número:")
numero = int(numero)

dobro = numero * 2

print("O dobro do número", numero, "é:", raiz_quadrada)

