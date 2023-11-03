# Variáveis de uma classe
class Computador:
    sistema_operacional = 'Windows 10'

    def __init__(self, marca, memoria_ram, placa_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_video = placa_video

    def ligar(self):
        print('Estou ligando o computador')

computador = Computador('Dell', '8gb', 'NVIDIA')
computador.marca = 'Asus'
print(computador.marca)
print(computador.sistema_operacional)

Computador.sistema_operacional = 'Mac'
computador2 = Computador('Asus', '2gb', 'ATI')
print(Computador.sistema_operacional)
