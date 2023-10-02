from datetime import datetime

# Decoretors
""" def pai(numero):
    def filho_1():
        print('Sou filho 1')
    def filho_2():
        print('Sou filho 2')
    if numero == 1:
        return filho_1

resultado = pai(1)
resultado()

def meu_decorator(funcao):
    def wrapper():
        print('Antes')
        funcao()
        print('Depois')
    return wrapper

@meu_decorator
def parabenizar():
    print('Parabéns')

parabenizar() """

def meu_decorator(funcao):
    def wrapper():
        print(datetime.now())
        funcao()
        print(datetime.now())
    return wrapper

@meu_decorator
def bom_dia():
    print('Bom dia')

bom_dia()