def palindromo(texto):
    texto = str(texto).replace(" ", "").lower()

    if texto == texto[::-1]:
        return f"{texto} é um palíndromo" 
    return f"{texto} não é um palíndromo"
print(palindromo("ovo"))