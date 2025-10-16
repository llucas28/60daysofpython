def busca_linear(lista, numero_procurado):
    """
    Procurar um número dentro de uma lista utilizando busca linear

    :parametro lista: lista de numeros
    :parametro numero_procurado: numero procurar
    """
    for i, numero in enumerate(lista):
        if numero == numero_procurado:
            return i
    return - 1

lista = [10,2,4,6,7,8,11]
numero_procurado = 11

buscando_o_numero = busca_linear(lista, numero_procurado)
print(buscando_o_numero)

if buscando_o_numero != -1:
    print(f"o numero se encontrando no indice: {buscando_o_numero}")
else:
    print("numero não encontrado")