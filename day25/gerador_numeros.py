import random

def gerar_numeros_aleatorios():

    numeros_aleatorios = []

    for _ in range(10):
        numero = random.randint(1, 100)
        numeros_aleatorios.append(numero)

    print("\nNúmeros aleatórios são: ")
    for i, numero in enumerate(numeros_aleatorios, start=1):
        print(f"Número {i} : {numero}")


if __name__ == "__main__":
    gerar_numeros_aleatorios()