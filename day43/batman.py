class Heroi:
    def __init__(self, nome, stamina):
        self.nome = nome
        self.stamina = stamina

    def usar_stamina(self, custo_stamina):
        try:
            if custo_stamina > self.stamina:
                raise ValueError("A stamina e insuficiente")
            self.stamina -= custo_stamina
            print(f"{self.nome} usou o golpe com sucesso.")
        except ValueError as Error:
            print(f"Erro: {Error}! O {self.nome} precisa recuperar stamina antes de continuar.")

if __name__ == "__main__":
    batman = Heroi(nome="Batman", stamina=50)
    batman.usar_stamina(custo_stamina=50)