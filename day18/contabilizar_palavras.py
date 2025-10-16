def contar_palavras(texto):
    
    palavras = texto.split()
    return len(palavras)

print(contar_palavras("oi tudo bem, como vai voce?"))