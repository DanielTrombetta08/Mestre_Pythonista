from flask import Flask, jsonify, request
from estrutura_banco_de_dados import Autor,Postagem, app, db


# Rota padrão - GET https://localhost:5000
@app.route('/')
def obter_postagens():
    return jsonify(postagens)

# Obter postagem por id - GET https://localhost:5000/postagem/1
@app.route('/postagem/<int:indice>', methods=['GET'])
def obter_postagem_por_indice(indice):
    return jsonify(postagens[indice])

# Criar uma nova postagem - POST https://localhost:5000/postagem
@app.route('/postagem',methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)

    return jsonify(postagem, 200)

# Alterar uma postagem existente - PUT https://localhost:5000/postagem/1
@app.route('/postagem/<int:indice>',methods=['PUT'])
def alterar_postagem(indice):
    postagem_alterada = request.get_json()
    postagens[indice].update(postagem_alterada)

    return jsonify(postagens[indice], 200)

# Excluir uma postagem - DELETE - https://localhost:5000/postagem/1
def excluir_postagem(indice):
    try:
        if postagens[indice] is not None:
            del postagens[indice]
            return jsonify(f'Foi excluído a postagem {postagens[indice]}',200)
    except:
        return jsonify('Não foi possível encontrar a postagem para exclusão',404)

# Obter autores
@app.route('/autores')
def obter_autores():
    autores = Autor.query.all()
    lista_de_autores = []
    for autor in autores:
        autor_atual = {}
        autor_atual['id_autor'] = autor.id_autor
        autor_atual['nome'] = autor.nome
        autor_atual['email'] = autor.email
        lista_de_autores.append(autor_atual)

    return jsonify({'autores': lista_de_autores})


# Obter autor por id
@app.route('/autores/<int:id_autor>',methods=['GET'])
def obter_autor_por_id(id_autor):
    autor = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor:
        return jsonify('Autor não encontrado!')
    autor_atual = {}
    autor_atual['id_autor'] = autor.id_autor
    autor_atual['nome'] = autor.nome
    autor_atual['email'] = autor.email
    lista_de_autores.append(autor_atual)
    
    return jsonify({'autor': autor_atual})


# Criar novo autor
@app.route('/autores',methods=['POST'])
def novo_autor():
    novo_autor = request.get_json()
    autor = Autor(nome=novo_autor['nome'], senha=novo_autor['senha'], email=novo_autor['email'])

    db.session.add(autor)
    db.session.commit()

    return jsonify({'mensagem': 'Usuário criado com sucesso'}, 200)


# Alterar autor
@app.route('/autores/<int:id_autor>',methods=['PUT'])
def alterar_autor(id_autor):
    usuario_a_alterar = request.get_json()
    autor = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor:
        return jsonify({'Mensagem': 'Este usuário não foi encontrado'})
    try:
        if usuario_a_alterar['nome']:
            autor.nome = usuario_a_alterar['nome']
    except:
        pass
    try:
        if usuario_a_alterar['email']:
            autor.email = usuario_a_alterar['email']
    except:
        pass
    try:
        if usuario_a_alterar['senha']:
            autor.senha = usuario_a_alterar['senha']
    except:
        pass

    db.session.commit()
    return jsonify({'mensagem': 'Usuário alterado com sucesso'})

# Excluindo autor
@app.route('/autores/<int:id_autor>',methods=['DELETE'])
def excluir_autor(id_autor):
    autor_existente = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor_existente:
        return jsonify({'mensagem': 'Este autor não foi encontrado'})
    db.session.delete(autor_existente)
    db.session.commit()

    return jsonify({'mensagem': 'Autor excluído com sucesso!'})


app.run(port=5000,host='localhost',debug=True)