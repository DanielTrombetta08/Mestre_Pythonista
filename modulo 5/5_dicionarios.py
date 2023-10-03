# Dicionários

pessoa = ['Carol', 18, 1.60]
# Dicionário (chave, valor)
dicionario_pessoa = {'nome': 'Carol', 'idade': 18, 'altura': 1.60}
pessoa_2 = dict(nome='Carol', idade=18, altura=1.60)
print(dicionario_pessoa)
print(pessoa_2)
print(pessoa_2['altura'])
print(dicionario_pessoa.keys())
print(dicionario_pessoa.values())
print(dicionario_pessoa.items())
# Iterar sobre um dicionário
for item in dicionario_pessoa.items():
    print(item)
    print(item[1])
    

