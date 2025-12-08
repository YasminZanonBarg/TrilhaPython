#%%
nome_arquivo = "historia_02.txt"
txt = "Meu novo arquivo!"

# mode = "r" | Modo de leitura padrão
# mode = "w" | Sobre reescreve todo o conteúdo
# mode = "a" | appenda os dados
with open(nome_arquivo, mode="w") as open_file:
    open_file.write(txt)