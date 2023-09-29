# Funções

def dar_boas_vindas():
    print('Boas Vindas')

dar_boas_vindas()

def dar_boas_vindas_personalizado(nome):
    print(f'Boas Vindas {nome}')

dar_boas_vindas_personalizado('Daniel')

# Valor Padrão
def apresentar_lugar(lugar='nossa loja'):
    print(f'Conheça {lugar}')

apresentar_lugar('Disney')

# DESAFIO 1 - Crie uma função chamada gerar_nome_completo que recebe como parâmetro o nome e sobrenome de alguém e dá boas vindas para essa pessoa
def gerar_nome_completo(nome, sobrenome):
    print(f'Boas Vindas {nome} {sobrenome}')

gerar_nome_completo('Daniel', 'Trombetta')
# DESAFIO 2 - # Crie uma função chamada calcular_valores que recebe 2 parâmetros o primeiro o preco de um produto e o segundo parâmetro é a quantidade, porém a quantidade deve haver um valor padrão de 1. Sua função deve exibir o resultado do preço do produto, multiplicado a quantidade escolhida.
def calcular_valores(preco, quantidade=1):
    print(preco * quantidade)

calcular_valores(12.5, 5)
