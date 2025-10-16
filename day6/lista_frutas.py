#frutas = ["banana", "maca", "uva", "pera", "manga" ]

#for frutas in frutas:
    #print(frutas)

frutas = []
while True:
		fruta = input("Digite o nome da fruta: ")
		if fruta == "sair":
			break
		frutas.append(fruta)

print(frutas)
