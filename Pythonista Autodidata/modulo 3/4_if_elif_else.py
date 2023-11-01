""" trabalho_terminado = True
if trabalho_terminado == False:
    print('Bora dar uma saida!')
else:
    print('Não posso sair')

velocidade = 60
if velocidade <= 50:
    print('Não foi multado')
elif velocidade >= 51 and velocidade <= 60:
    print('Levou multa de 2 pontos')
elif velocidade > 61 and velocidade <= 75:
    print('Levou multa de 3 pontos')
else:
    print('Levou multa de 7 pontos')

# Chaining
if velocidade <= 50:
    print('Não foi multado')
elif 51 <= velocidade <= 60:
    print('Levou multa de 2 pontos')
elif 61 <= velocidade <= 75:
    print('Levou multa de 3 pontos')
else:
    print('Levou multa de 7 pontos') """


# Monte o seguinte cenário usando condicionais

# Você está montando um sistema para um salão de beleza para calcular o preço do corte de cabelos grandes que irá seguir as seguinte regras

# Disclaimer the haircut values are completely ficticious, I have no ideia of actual prices

cabelo = 60
#Se seu cabelo estiver com ou abaixo de 20cm você paga o valor de R$50,00
if cabelo <= 20:
    print('Valor R$ 50,00')
#Se seu cabelo estiver entre 21cm a 30cm você paga o valor de R$70,00
elif 21 <= cabelo <= 30:
    print('Valor R$ 70,00')
#Se seu cabelo estiver entre 31cm a 50cm você paga o valor de R$100,00
elif 31 <= cabelo <= 50:
    print('Valor R$ 100,00')
#Acima de 50cm Favor consultar na recepção
else:
    print('Favor consultar!')
# Declare uma variável que represente o tamanho atual do cabelo

# Apenas imprima na tela a mensagem apropriada, nada além disso é necesário
