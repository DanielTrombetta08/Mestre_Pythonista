import json

with open('desafio.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data['user'][1]['email'])

with open('desafio.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data['user'][0]['address']['city'])

with open('desafio.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data['user'][1]['orders'][0]['total'])


