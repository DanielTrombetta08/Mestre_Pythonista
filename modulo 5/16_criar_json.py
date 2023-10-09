import json
# Criar iu ler JSON
computador_json = """{
    "marca": "Dell",
    "preço": 15000
}"""
# Lendo um strong JSON
data = json.loads(computador_json)
print(data)
# Salvar um string JSON -> Criar Arquivo JSON
 with open('computador.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(computador_json, arquivo_json) 
# Para ler um arquivo JSON
with open('computador.json', encoding='utf-8') as arquivo_json:
    string = json.load(arquivo_json) # convertendo JSON -> String
    dicionario = json.loads(string) # Converter de String -> Dicionário Python
    print(dicionario['marca'])


