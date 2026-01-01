def dividir(numerador, denominador):
    try:
        resultado = numerador / denominador
        print(f"O resultado da divisao e {resultado}")
    except ZeroDivisionError:
        print("A divisao por 0 nao pode ocorrer")
    except TypeError:
        print("O codigo nao pode aceitar strings apenas numeros")
    print("Funcao rodou")

if __name__ == "__main__":
    dividir (5,5)