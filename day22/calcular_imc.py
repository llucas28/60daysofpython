def calcular_imc():
    print("Bem-vindos à calculadora de IMC")

    try:
        peso = float(input("Digite o seu peso em quilogramas: "))
        altura = float(input("Digite sua altura em metros: "))

        if peso <= 0 or altura <= 0:
            print("O peso e a altura devem ser maiores que 0")
            return

        imc = round(peso / (altura ** 2), 1)

        if imc < 18.5:
            mensagem = "Você está abaixo do peso ideal."
        elif imc < 25:
            mensagem = "Você está no peso normal."
        elif imc < 30:
            mensagem = "Você está de sobrepeso."
        else:
            mensagem = "Você está com obesidade."

        print(f"Seu IMC é {imc}. {mensagem}")

    except ValueError:
        print("A entrada está inválida")

if __name__ == "__main__":
    calcular_imc()