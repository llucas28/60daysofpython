numero = int(input("Digite o núemro para verificar se ele é primo: "))

primo = True

if numero <= 1:
    primo = False

for i in range(2, int(numero ** 0.5) + 1):
    if numero % i == 0:
        primo = False
        break

if primo:
    print(f"{numero} é um número primo")
else:
    print(f"{numero} não é um número primo")
