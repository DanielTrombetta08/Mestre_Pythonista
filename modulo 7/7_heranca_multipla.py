# Herança Múltipla
class Pessoa:
    nome = 'Sou uma pessoa'

    def convidar(self):
        print('Olá sou uma pessoa, vamos ao evento')

class Profissional:
    nome = 'Sou um profissional'

    def convidar(self):
        print('Olá sou um profissional, vamos ao evento')

class AtorProfissional(Pessoa, Profissional):
    pass

ator_profissional = AtorProfissional()
ator_profissional.convidar()
print(AtorProfissional.mro())

