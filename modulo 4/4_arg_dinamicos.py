# Argumentos Dinâmicos
# Usando simbolo * para passar mais de um valor para a variável
# *args
# Variáveis simples precisam ser nomeadas
def somar(*valores, b):
    print(valores)
    for valor in valores:
        b += valor
    print(b)

somar(10,20,5, b=5)