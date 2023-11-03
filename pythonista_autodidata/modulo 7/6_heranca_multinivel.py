# Herança multinível
# 1º Problema
class Veiculo:
    pass
class VeiculoDeRodas(Veiculo):
    quantidade_maxima_de_rodas = 2
    pass
class Carro(VeiculoDeRodas):
    pass
class CarroEletrico(Carro):
    pass
class CarroEletricoDuasPortas(CarroEletrico):
    pass

# Evitar usar esse tipo de herança