# Processar vs Retornar
# Função que apenas processa dados
print('Ola')
# Funções que retornam dados
#cidade = input('Qual a sua cidade? ')

# Como escolher entre funções que processam ou retornam dados?
# Eu vou precisar usar essa informação na lógica do meu programa ainda?
# Ou só preciso processar esse dado, mas não irei utilizar mais ele depois?
def exibir_cotacao_moeda(moeda):
    if moeda == 'usd':
        print(5.47)
exibir_cotacao_moeda('usd')

def obter_cotacao_moeda(moeda):
    if moeda == 'usd':
        return 5.47

cotacao = obter_cotacao_moeda('usd')
if cotacao > 5:
    print('Investir')
else:
    print('Não investir')

    