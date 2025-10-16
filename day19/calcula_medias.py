def calcular_media_notas(notas):


    media = sum(notas) / len(notas)
    return round(media, 2)

print(calcular_media_notas([10,4,5,6,9]))