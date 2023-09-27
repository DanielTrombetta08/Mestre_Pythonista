from datetime import datetime
from random import choice
## Objetivo de projeto

# * Estamos criando um módulo de login do nosso aplicativo, e você deve obter as seguintes informações do funcionário.

## Módulo 1 - Gerar registro do funcionário

### Funcionalidades do módulo 1


#1. Obtenha o nome do usuário
nome = str(input('Nome: '))
#2. Obtenha a idade do usuário
idade = int(input('Idade: '))
#3. Registre de forma automática a data do cadastro do usuário, usando a data do registro como data de registro
data_cadastro = datetime.now()
#data_cadastro = datetime.strptime(data_cadastro, '%d/%m/%Y')
print(data_cadastro)
#4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, que é sorteado de forma aleatória:


cartoes = ['R$50,00','R$250,00','R$120,00']


#5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)
data_aniversario = datetime.strptime(input('Data de Aniversário: '), '%d/%m/%Y')

## Módulo 2 - Gerar apresentação do usuário

### Funcionalidades do módulo 2 - Mensagem de boas vindas!
print('Boas Vindas!')
#Usando os dados obtidos no módulo 1, exiba as seguintes informações:

#1. Olá (nome do usuário), seu registro foi concluído com sucesso no dia(data de cadastro no formato dd/mm/aaaa).
print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {data_cadastro.day}/{data_cadastro.month}/{data_cadastro.year}\nParabéns você ganhou um cartão de compras no valor de {choice(cartoes)}')
#Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de (valor sorteado).