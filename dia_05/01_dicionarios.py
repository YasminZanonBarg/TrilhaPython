#%% Pares de chave/valor
dicionario_teo = {
    "nome":"Téo",
    "sobrenome":"Calvo",
    "filhos":True,
    "formação":["estatística", "bigdata datascience"],
    "cargos":[
        {"nome":"ds jr", "empresa":"tapps"},
        {"nome":"ds pl", "empresa":"sas"},
        {"nome":"ds sr", "empresa":"boticario"},
        {"nome":"ds espec.", "empresa":"via varejo"},
    ]
}

print(dicionario_teo)

# exemplo de acesso as chaves
# Qual é a empresa atual do teo?
dicionario_teo["cargos"][-1]["empresa"]

# Dicionários são muito utilizados em API
# JSON é uma aplicação de dicionário



#%% Adicionando novos valores ao dicionário
dicionario_teo["estado civil"] = "casado"
print(dicionario_teo)



#%% Métodos
# Descobrir os nomes das chaves
dicionario_teo.keys()

# Descobrir os valores
dicionario_teo.values()

# Pares chaves e valores
dicionario_teo.items() # retorna uma tupla



#%% Percorrendo um dicionário
for chave in dicionario_teo:
    print(chave, "->", dicionario_teo[chave])

# ou
for item in dicionario_teo.items():
    print(item)
    
# ou (unpacking >>> descacoplando as chaves de valores)
for chave, valor in dicionario_teo.items():
    print(chave, "->", valor)