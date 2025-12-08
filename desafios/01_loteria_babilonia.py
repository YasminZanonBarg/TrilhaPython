# Construa um programa que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado.
# Caso o usuário acerte, dê os parabéns.

import random

# Antes de iniciar as condicionais, será feito uma validação do input do usuário
def get_input():
    while True:
        try:
            numero_usuario = int(input("Entre com um número: "))
        
        except ValueError as err:
            print("Valor inválido!")
            continue # Serve para continuar repetindo o laço até não está mais com erro

        if not 1 <= numero_usuario <= 15:
            return numero_usuario

        print("Valor inválido! O valor deve ser entre 1 e 15")

def check_numbers(numero_sorteio, numero_usuario):
    if numero_sorteio == numero_usuario:
        print("Parabéns!")
        return True

    elif numero_usuario > numero_usuario:
        print("Número muito alto, Tente um número menor!")    
        return False

    else: 
        print("Número muito baixo, Tente um número maior!")  
        return False

numero_sorteio = random.randint(1,15)

for tentativa in range(3):
    numero_usuario = get_input()
    if check_numbers(numero_usuario=numero_usuario, numero_sorteio=numero_sorteio):
        break

# Caso o for não finalizar com um break, ele vai usar esse else do for
else:
    print("Suas tentativas acabaram!!")    