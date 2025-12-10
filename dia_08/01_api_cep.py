import requests # para realizar requisiçoes na web
import json     # para tratar json de listas/dicionário para arquivos json 
from tqdm import tqdm
import pandas as pd

ceps = [
    "88354310",
    "88350100",
    "88360000",
    "01519000",
    "13329120"
]

url = "https://viacep.com.br/ws/{cep}/json/"

data = []

for cep in tqdm(ceps):
    response = requests.get(url.format(cep=cep))
    if response.status_code == 200:
        data.append(response.json())

#%% 
dataset = pd.DataFrame(data)
dataset.to_csv("ceps.csv", sep=";")


#%% Salvando os dados
with open("ceps.json", "w", encoding='utf-8') as open_file:
    json.dump(data, open_file, ensure_ascii=False, indent=4)
