#%% 1) Fazendo a leitura do meu arquivo CSV
nome_arquivo = "C:/Users/114954/Documents/Projetos/Python - TeoMeWhy/curso_python/dia_07/data.csv"

with open(nome_arquivo) as open_file:
    # readlines = Cada registro é um elemento na lista
    data = open_file.readlines()
    print(data)

for linha in data:
    print(linha)



#%% 2) Desenvolvendo um dicionário que me devolva a seguinte estrutura:
# {
#     'nome': ['TÃ©o', 'Nah', 'Claudio', 'Kozato'],
#     'idade': ['32', '35', '42', '22'],
#     'profissao': ['streamer', 'artesa', 'dev', 'ml-engineer']
# }

chaves = data[0].strip("\n").split(";")
dados = dict()


for elemento in chaves:
    dados[elemento] = []


# Percorrendo todas as linhas apartir da segunda
for linha in data[1:]:

    # Removendo /n e separando por ;
    valores = linha.strip("\n").split(";")
    
    # Passando no dicionário dados os valores
    for i in range(0, len(valores)):

        # Atribuindo para cada chave seu valor no indexe correspondente
        dados[chaves[i]].append(valores[i])

dados



#%% 3) Apartir dos dados prontos calcular media da idade dessas informações
idades = []

for i in dados["idade"]:
    idades.append(int(i))

media = sum(idades) / len(idades)
media