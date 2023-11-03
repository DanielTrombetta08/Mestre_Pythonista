# Desafio 1
lista = [2 * i for i in range(1,6)]
#print(lista)

# Desafio 2
cores = ['vermelho', 'azul', 'verde', 'amarelo', 'rosa', 'preto']

print([str(cores.index(cor)+1) + ' - ' + cor for cor in cores])

# Desafio 3
participantes = ['joel', 'jessica', 'maria', 'cris', 'larissa']
pagamento_realizado = ['joel', 'jessica']

print([i + ' Pago' if i in pagamento_realizado else i + ' Devendo' for i in participantes])