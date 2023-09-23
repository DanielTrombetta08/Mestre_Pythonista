# Erro Genérico
# 1 - Leia o erro
# 2 - Copie a msg e cole no google tradutor
# 3 - Tente entender o que fazer a partir da mensagem
nome = 'amanda'
       #012345
print(nome[6])

# Erro específico(inclui dados da sua aplicação)
with open('senhas.txt','r') as arquivo:
    for linha in arquivo:
        print(linha)
# FileNotFoundError: [Errno 2] No such file or directory: 'senhas.txt'
# Usar a parte genérica sem a informação específica: FileNotFoundError: [Errno 2] No such file or directory: