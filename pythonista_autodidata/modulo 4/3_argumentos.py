def exibir_preco(produto, preco):
    print(f'{produto} está no valor de: {preco}')

# Argumentos posicionais
exibir_preco('Iphone', 5000)

exibir_preco(produto='Iphone', preco=5000)
# Argumentos nomeados
exibir_preco(preco=5000, produto='Iphone')

# Simbolo * deixa todos os argumentos nomeados a partir dele
def exibir_preco(produto, *, preco):
    print(f'{produto} está no valor de: {preco}')

def gerar_objeto_personalizado(cor, *, altura, formato):
    print(cor, altura, formato)

gerar_objeto_personalizado('verde', altura=1.80, formato='redondo')

