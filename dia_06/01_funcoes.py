#%% Exemplo de funções nativas
print()
sum()
input()

#%% Criando uma função de soma
def f(x):
    return 1 + x

# executando função desenvolvida
f(10)


#%% Função de juros compostos
# TypeHint: atrás dos parametros informar a tipagem dos mesmos 
#           + "->" o valor após informa o tipo de dado que será retornado da função 
def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    # DocString: Agora quando eu passar o mouse em cima linha da chamada de função eu irei ter essa descrição 
    """
        juros_compostos serve para calcular o retorno financeiro a partir de um aporte.
        Deve-se considerar o valor, a taxa de juros atual e o tempo (em anos) para o cálculo ser retornado.
    
        aporte:
            um número inteiro, que represente o valor em R$

        taxa:
            um número float entre 0 e 1 que represente o valor taxa de juros

        anos:
            um número inteiro >= 1 que representa o tempo que o investimento terá liquidez
    """
    return aporte * (1 + taxa) ** anos

# Boa prática: mantém a ordem e mantenha escrito o nome dos parametros na frente
juros_compostos(aporte=1000, taxa=0.13, anos=4)


# obs: para mais boas práticas lei o zen de python