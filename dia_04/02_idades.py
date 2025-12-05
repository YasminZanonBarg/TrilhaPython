#%% Métodos das listas

idades = [17, 32, 56, 87]

# Para saber os métodos existentes use "."
# exemplos:
# 1. incluindo novo elemento no final
idades.append(32)
print(idades)


#%%
# Programa para criar uma lista de idades e retornar estátistica

idades = []

while True:
    idade = input("Entre com a idade: ")

    if idade == "":
        break

    idades.append(int(idade))

media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtde_idades = len(idades)

print("MEDIA:", media)
print("MINÍMO:", minimo)
print("MÁXIMO:", maximo)
print("QTDE ELEMENTOS:", qtde_idades)

# shift + alt + i = Final das linhas selecionadas
# home = Início linhas
# ctrl + shift + seta = Selecionar palavras
