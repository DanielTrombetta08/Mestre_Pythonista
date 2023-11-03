# Como usar uma list comprehension
nova_lista = [2 * i for i in range(10)]
# [expressão for membro in iterável]
print(nova_lista)

def aprovar_pessoa(nome):
    # Lógica mais complexa
    return nome + ' Aprovado'


nomes = ['Larissa', 'Rafael', 'Marcos', 'João']
print([nome + ' Aprovado' for nome in nomes])

print([aprovar_pessoa(nome) for nome in nomes])

from pprint import pprint

pprint([[i for i in range(1,6)] for x in range(5)])

# Usar condicionais
# [expressão for membro in iterável (condicional if)]
print([aprovar_pessoa(nome) for nome in nomes if nome != 'Rafael'])
# Valores numéricos
print([i for i in range(20) if i not in (1,5,15,19)])

def eh_numero_par(numero):
    valor = numero % 2
    if valor == 0:
        return True
    else:
        return False
    
print([i for i in range(20) if eh_numero_par(i)])

# Condicional flexível
# [expressão (condicional if) for membro in iterável]
participantes = ['Larissa', 'Rafael', 'Marcos', 'João']
ganhadores = ['Larissa', 'Rafael']
print([i + ' Ganhador' if i in ganhadores else i + ' Não selecionado' for i in participantes])


