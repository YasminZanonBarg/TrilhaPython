# Programa valida se o usuário pode beber cerveja
# Otimização de código = Com a nova condição de idade, se o usuário tiver idade maior que 70, com dois ifs, ele vai printar as duas condicoes
idade = int(input("Qual é a sua idade?"))

if idade > 70:
    print("Cuidado com a bebida, consulte com o seu médico")
elif idade >= 18:
    print("Você pode beber cerveja!")
else:
    print("Você não pode beber cerveja!")
