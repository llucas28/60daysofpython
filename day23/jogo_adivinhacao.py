import random

def jogo_adivinhacao():


    print("Bem vindos ao nosso jogo de adivinhação")


    numero_secreto = random.randint(0, 100)

    tentativas = 0

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < numero_secreto:
                    print("Muito abaixo do número secreto.")
            elif palpite > numero_secreto:
                    print("Muito alto em relação ao número secreto.")
            else: 
                    print(f"Parabéns você acertou o número era {numero_secreto}, suas tentivas foram {tentativas}.")
                    break
        except ValueError:
            print("Por favor, digite um número válido.")        

if __name__ == "__main__":
    jogo_adivinhacao()