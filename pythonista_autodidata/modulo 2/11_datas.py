from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

# Criar uma data
lancamento_app = datetime(2023,5,28)
print(lancamento_app)
# Quero receber a data de lançamento
# 25/08/2023
data_lancamento = datetime.strptime(input('Quando devemos lançar o aplicativo? '), '%d/%m/%Y')
print(data_lancamento)
print(type(data_lancamento))
# Intervalo entre datas
data_atual = datetime.now()
prazo = data_lancamento - data_atual
print(prazo.days)
