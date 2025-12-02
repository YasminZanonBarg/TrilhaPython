# Programa valida se o usuário pode beber cerveja
# Otimização de código = Com o else não preciso validar todos os if's
idade = int(input("Qual é a sua idade?"))

if idade >= 18:
    print("Você pode beber cerveja!")
else:
    print("Você não pode beber cerveja!")
