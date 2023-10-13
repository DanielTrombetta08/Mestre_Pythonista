# Classes Abstratas
# Criar um contrato(esqueleto) que deve ser implementado na classe que a herda
from abc import ABC, abstractclassmethod

class Camera(ABC):
    @abstractclassmethod
    def definir_tamanho_lente(self, tamanho):
        pass

class CameraProfissional(Camera):
    def definir_tamanho_lente(self, tamanho):
        print(f'Alterando a lente para {tamanho}')

camera_profissional = CameraProfissional()
camera_profissional.definir_tamanho_lente(5)

class Monitor(ABC):

    @abstractclassmethod
    def aumentar_claridade(self, percentual):
        pass

    @abstractclassmethod
    def diminuir_claridade(self, percentual):
        pass

class MonitorFullHD(Monitor):
    def aumentar_claridade(self, percentual):
        print(f'Aumentando a claridade em {percentual}%')

    def diminuir_claridade(self, percentual):
        print(f'Diminuindo a claridade em {percentual}%')

monitor_full_hd = MonitorFullHD()
monitor_full_hd.aumentar_claridade(5)
monitor_full_hd.diminuir_claridade(5)


