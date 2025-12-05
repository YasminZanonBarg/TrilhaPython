#%%
lista_teo = [32, 1, "Casado", "dev goLang"]
lista_teo

#%%
# Adicionando item na lista
lista_teo.append(123)
# Substituindo valor da primeira posição
lista_teo[0] = 33

#%% DEFINIÇÃO DE TUPLA = São listas que não podem ser alteradas (não possuem métodos como append, remove ...). São imutaveis.
# tupla_teo = 32, 1, "Casado", "dev goLang"
tupla_teo = (32, 1, "Casado", "dev goLang", ["ds jr", 'ds pl', 'ds sr'])
type(tupla_teo)

# obs: consigo adicionar apenas os itens em objeto mutavel como a lista dentro da tupla
tupla_teo[-1].append("ds espec")
tupla_teo