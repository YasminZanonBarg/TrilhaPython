#%% Manipulação de arquivos no python
nome_arquivo = "C:/Users/114954/Documents/Projetos/Python - TeoMeWhy/curso_python/dia_07/historia.txt"

# Abre arquivo em formato de leitura
open_file = open(nome_arquivo)

# Lê os dados do arquivo
conteudo = open_file.read()
print(conteudo)

# Sempre fechar o arquivo que está sendo manipulado, isso garante que ele não será corrompido
open_file.close()



#%% Como podemos esquecer de fechar o arquivo a forma mais usual de fazer o que foi mostrado a cima é:
#   Utilizando o "with" toda a manupulação é feito no escopo e depois quando termina já finaliza automaticamente
nome_arquivo = "C:/Users/114954/Documents/Projetos/Python - TeoMeWhy/curso_python/dia_07/historia.txt"

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()