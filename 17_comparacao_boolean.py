# Esemplo 1
idade = 21
possui_convite = False
filho_do_dono = True
#print(idade >= 21 and possui_convite == True)
# maior de 21 e possui convite ou seja filho do dono
#print((idade >= 21 and possui_convite) or (filho_do_dono))

# Exemplo 2
maior_de_idade = True
possui_carteira_trabalho = True
trabalhando_atualmente = True
possui_veiculo = False
# maior de idade e possui carteira de trabalho
#print(maior_de_idade and possui_carteira_trabalho)
# não possui veiculo prórpio e possui carteira de trabalho
#print(possui_carteira_trabalho and not possui_veiculo)

possui_passaporte = False
passagem_comprada = False
menor_de_idade = False

print((possui_passaporte and passagem_comprada) and not menor_de_idade)
print((possui_passaporte or passagem_comprada) and not menor_de_idade)
print((not possui_passaporte or passagem_comprada) and not menor_de_idade)
print((not possui_passaporte or not passagem_comprada) and menor_de_idade)
print((possui_passaporte and passagem_comprada) and not menor_de_idade)
