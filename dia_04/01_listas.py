#%% Listas = forma de armazenar mais de um valor em uma váriavel
lista_idades = [12, 13, 14, 15, 16, 17]
print(lista_idades)


# Funções:

# Exibir tipo
type(lista_idades)

# Soma de todas as idades
print("soma idades:", sum(lista_idades))

# Quantidade de elementos na lista
print("elementos idades:", len(lista_idades))

# Média de todas as idades
print("média idades:", sum(lista_idades) / len(lista_idades))

# Menor valor da lista
print("menor idades:", min(lista_idades))

# Maior valor da lista
print("maior idades:", max(lista_idades))


#%% Listas são do tipo de dados listas e elas podem armazerar diversos tipos de dados
teo = ["Teo Calvo", 
       32, 
       True, 
       "Casado",
       ["estagiario,", "ds junior", "ds pleno", "ds senior", "head"],
       [1500, 4000, 5000, 6500, 10000], 
       ["Ana", "Maria", "Claudia"]
    ]

print("Tamanho da lista téo: ", len(teo))

# Como acessar um indexe da lista?
# idade
print(teo[2])
# renda
print(teo[5])
# primeiro nome
print(teo[0])


# Acessando última lista e pegando o último elemento
print(teo[6][2])
# ou
print(teo[-1][-1])


# Fatiando minha lista 
# ex1: os 4 primeiro elementos
print(teo[0:4])
print(teo[:4]) # Para o 0 não precisa colocar

#ex2: quais foram as últimas 2 posições de mercado do teo
print(teo[4][-2:]) 


#%% 
# O fatiamento funciona da seguinte maneira:
# lista[ start_indexe : stop_indexe : navigation_rule ]

# Ordenar os salário do maior para o menor
salarios = teo[5]
salarios[::-1]

# Pular os salários elementos
salarios[::2]
