def tabuada():
    try:
        numero = int(input("Digite um número para gerar a tabuada: "))

        print (f"\nTabuada de {numero}:")

        for i in range (1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")

    except ValueError:
            print("Entrada inválida. Digite um número")
        
if __name__ == "__main__":
    tabuada()