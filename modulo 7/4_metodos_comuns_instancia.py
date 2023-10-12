class Computador:
    sistema_operacional = 'Windows 10'

    # Métodos comuns(self)
    def __init__(self, marca, memoria_ram, placa_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_video = placa_video

    def exibir_dados_do_computador(self):
        print(self.marca, self.memoria_ram, self.placa_video, self.sistema_operacional)

    # Métodos de Classe(Class Methods)
    @classmethod
    def computador_escritorio(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de vídeo - Baixo Custo')
    
    @classmethod
    def computador_configuracao_pesado(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de vídeo - Alto Nível')
    
    # Metodos Estáticos(Static Methods)
    @staticmethod
    def roda_programas_pesados(memoria_ram):
        if memoria_ram >= 8:
            return True
        else:
            return False
# Configuração p/ cliente de escritório
computador1 = Computador.computador_escritorio('8gb')
# Configuração p/ cliente de trabalho pesado(jogos, vídeos, 3d)
computador2 = Computador.computador_configuracao_pesado('16gb')
computador1.exibir_dados_do_computador()
computador2.exibir_dados_do_computador()

print(Computador.roda_programas_pesados(10))
    

