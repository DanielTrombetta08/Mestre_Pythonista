# Classe
class Computador:
    def __init__(self, marca, memoria_ram, placa_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_video = placa_video

computador1 = Computador('Asus', '8gb', 'Nvidia')
print(computador1.marca)
print(computador1.memoria_ram)
print(computador1.placa_video)

computador2 = Computador('Dell', '4gb', 'ATI')
print(computador2.marca)
print(computador2.memoria_ram)
print(computador2.placa_video)
       