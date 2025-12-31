class Veiculo:
    def __init__(self, marca, modelo, velocidade_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima

    def ligar_motor(self):
        print(f"O carro foi ligado, o modelo e {self.modelo} e a marca e {self.marca}")

    def acelerar(self):
        print(f"O {self.modelo} esta acelerando a velocidade de ate {self.velocidade_maxima} por hora")
    
    def ligar_luzes(self):
        print(f"O {self.modelo} da marca {self.marca} ligou as luzes")

class Carro(Veiculo):
    def __init__(self, marca, modelo, velocidade_maxima, portas):
        super().__init__(marca, modelo, velocidade_maxima)
        self.portas = portas

    def abrir_portas(self):
        print(f"Abrindo as {self.portas} portas do {self.marca} {self.marca}")


#meu_veiculo = Veiculo(marca="Toyota", modelo="Corolla", velocidade_maxima=160)

#meu_veiculo.acelerar()
#meu_veiculo.ligar_motor()

meu_carro = Carro(marca="Toyota", modelo="Corolla", velocidade_maxima=160, portas=4)

meu_carro.acelerar()
meu_carro.ligar_motor()
meu_carro.ligar_luzes()
meu_carro.abrir_portas()