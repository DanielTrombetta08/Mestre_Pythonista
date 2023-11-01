# Polimorfismo
""" print(10 +20)
print('Olá' + ' Dev')

print(len('Livro'))
print(len([25, 20, 30]))
print(len({'Título': 'Livro 1', 'Lançamento': '2010', 'Categoria': 'Romance'})) """

class Carro:
    def ligar(self):
        print('Ligando o carro')

class Moto:
    def ligar(self):
        print('Ligando a moto')

def iniciar(veiculo):
    veiculo.ligar()

carro = Carro()
moto = Moto()

iniciar(carro)
iniciar(moto)

class Pessoa:
    def apresentar(self, nome, idade=None, profissao=None):
        if idade and profissao != None:
            print(nome, idade, profissao)
        elif idade != None:
            print(nome, idade)
        elif profissao != None:
            print(nome, profissao)
        else:
            print(nome)

pessoa = Pessoa()
pessoa.apresentar('Amanda')
pessoa.apresentar('Amanda', 18)
pessoa.apresentar('Amanda', 18, 'Programadora')
