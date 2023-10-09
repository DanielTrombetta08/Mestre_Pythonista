import json
pessoa = """{
    "name": "John Smith",
    "age": 30,
    "city": "New York",
    "isStudent": true,
    "gpa": 3.5
}"""
data = json.loads(pessoa)
print(data)

with open('desafio2.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(pessoa, arquivo_json)