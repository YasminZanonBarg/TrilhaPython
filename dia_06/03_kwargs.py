#%% Criar uma função para calcular o valor do imposto de um produto
#   **kwargs = se comporta como um dicionário (chave/valor)

def calc_imposto(preco:float, tx_base:float, **kwargs):
    imposto = preco * tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]
    
    return imposto

# 1) forma de chamar o **kwargs
calc_imposto(
    preco=100, 
    tx_base=0.03, 
    municipio=0.01, 
    estadual=0.005, 
    nacional=0.001
)

# 2) forma de chamar o **kwargs
impostos_gerais = {
   "municipio":0.01, 
   "estadual":0.005, 
   "nacional":0.001
}

calc_imposto(
    preco=100, 
    tx_base=0.03, 
    **impostos_gerais
)