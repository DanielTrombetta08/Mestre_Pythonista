import json

with open('usuarios1.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data['nome'])
# break point -> F9 -> F5 -> F10 -> console depuração

with open('usuarios2.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data['permissões'][1])

with open('usuarios3.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data['usuários'][0]['telefone'])

with open('usuarios4.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data['usuários'][0]['plano']['preco'])

with open('usuarios5.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data[0]['admin'])
    


