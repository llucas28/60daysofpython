def conversor_moeda(valor, taxa_cambio, tipo_conversao):
    if tipo_conversao == 'dolar_real':
        return round(valor * taxa_cambio, 2)
    elif tipo_conversao == 'real_dolar':
        return round(valor / taxa_cambio, 2)
    else:
        return ValueError ("Esse tipo de conversão não é válida")

print(conversor_moeda(10, 5.41, 'dolar_real'))
print(conversor_moeda(10, 5.41, 'real_dolar'))
