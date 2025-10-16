def pode_dirigir(idade):
    if idade >= 18:
        return True
    else:
        return False

try:
    input_user = int(input("Digite sua idade: "))
    print(pode_dirigir(input_user))
except ValueError:
    print("Entrada invalida. Por favor, digite um número inteiro.")