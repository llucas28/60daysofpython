def contador_personalizado():
    try:
        limite = int(input("Digite o valor máximo do contador: "))
        
        limite = limite + 1
        for i in range(limite):
            print(i)
            if i == limite:
                print("Contador atingiu o limite")
                #break
    except ValueError:
        print("Entrada invalida. Por favor insira um numero inteiro")

contador_personalizado()