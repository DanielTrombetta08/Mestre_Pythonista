from flask import Flask, jsonify, request

app = Flask(__name__)

musicas = [
    {
        "canção": "Sweet Child O'Mine",
        "banda": "Guns N Roses"
    },
        {
        "canção": "Amor Clandestino",
        "banda": "Maná"
    },
        {
        "canção": "Help",
        "banda": "Beatles"
    }
]

# GET
@app.route('/')
def obter_musicas():
    return jsonify(musicas)

# GET by ID
@app.route('/musicas/<int:indice>', methods=['GET'])
def obter_musica_por_id(indice):
    return jsonify(musicas[indice])

# POST
@app.route('/musicas', methods=['POST'])
def nova_musica():
    musica = request.get_json()
    musicas.append(musica)
    return jsonify(musica, 200)
# Body - Raw - JSON - digitar a postagem em formato de dicionário JSON

# PUT
@app.route('/musicas/<int:indice>', methods=['PUT'])
def alterar_musica(indice):
    musica_alterada = request.get_json()
    musicas[indice].update(musica_alterada)
    return jsonify(musicas[indice], 200)
# Body - Raw - JSON - digitar a postagem em formato de dicionário JSON

# DELETE
@app.route('/musicas/<int:indice>', methods=['DELETE'])
def excluir_musica(indice):
    try:
        if musicas[indice] is not None:
            del musicas[indice]
            return jsonify(f'Música {musicas[indice]} foi excluida!', 200)
    except:
        return jsonify('Não foi possível encontrar a música para exclusão!', 404)
        
app.run(port=5000, host='localhost', debug=True)