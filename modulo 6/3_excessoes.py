internet = None
try:
    print('Fazendo conexão com a ' + internet)
except TypeError as erro:
    print('Não há conexão com a internet')
finally:
    print('Desfazendo a compra!')

try:
    valor = int(input('Digite um valor: '))
    print(valor / 0)
except ZeroDivisionError as erro:
    print('Não é possível dividir por zero')
except ValueError as erro:
    print('Favor digitar apenas números')
finally:
    print('Operação cancelada')
      