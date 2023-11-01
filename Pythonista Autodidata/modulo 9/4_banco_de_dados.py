# db.sqlite3
import sqlite3

with sqlite3.connect('artistas.db') as conexao:
    # Criar uma conexão com o banco de dados
    sql = conexao.cursor()
    # Rodar Comando SQL
    sql.execute('create table bandas(nome text, estilo text, membros integer);')
    # Exemplo de inserir dados
    sql.execute('insert into bandas(nome, estilo, membros) values ("Banda 1", "Rock", 3)')
    # Exemplo de usar dados da minha aplicação em uma consulta SQL
    nome = input('Digite o nome da banda: ')
    estilo = input('Digite o estilo da banda: ')
    quantidade_integrantes = int(input('Quantidade de integrantes da banda: '))

    sql.execute('insert into bandas values(?,?,?)', [nome, estilo, quantidade_integrantes])
    # Salvando alterações no banco de dados
    conexao.commit
    # Exibir dados no console python(terminal)
    bandas = sql.execute('select * from banda;')
    for banda in bandas:
        print(banda)
