# Boa prática: O ideal é uma função ter apenas um objetivo específico.
# Dessa forma a função fica modular e posso utiliza-la em outros momentos, 
# inclusive dentro de outras funções
def soma(a:float, b:float)->float:
    return a + b

# Argumentos opcionais dentro de uma função OBRIGATORIAMENTE devem estar por último e "=0"
def media(a:float, b:float)->float:
    return soma(a,b) / 2

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))

print("Média:", media(a,b))

#%% Comportamento de somar duas listas
a = [1, 2, 3]
b = [4, 5, 6]
a + b

#%% *args = 0 ou mais atributos que não sabemos quando serão
#   args são do tipo tupla
#   args são uma convesão, se eu colocar *parametros também funciona

def soma(a:float, b:float, *args)->float:
    valores = [a,b] + list(args)
    return sum(valores)

def media(a:float, b:float, *args)->float:
    return soma(a, b, *args) / len(args)+2

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))
d = float(input("Entre com o valor de d: "))
e = float(input("Entre com o valor de e: "))
f = float(input("Entre com o valor de f: "))

print("Média:", media(a,b,c,d,e,f))