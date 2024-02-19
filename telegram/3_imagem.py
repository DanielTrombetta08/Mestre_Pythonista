# TOKEN 5790788365:AAHA0RU0YkD8Ywuwfem1D8RDy7PftroNWeU
# URL do API - https://api.telegram.org/bot5790788365:AAHA0RU0YkD8Ywuwfem1D8RDy7PftroNWeU/getUpdates
# Qual tipo de requisição quer fazer
import requests
from rich import print
from time import sleep


def obter_mensagens(apenas_ultima_mensagem=False):
    update_id = None
    token = '5790788365:AAHA0RU0YkD8Ywuwfem1D8RDy7PftroNWeU'
    data = requests.get(f'https://api.telegram.org/bot{token}/getUpdates')
    if len(data.json()['result']) > 0:
        if apenas_ultima_mensagem == True:
            update_id = data.json()['result'][-1]['update_id']
            data = requests.get(
                f'https://api.telegram.org/bot{token}/getUpdates?offset={update_id}')
            print(data.json())
            print('#'*10)
        else:
            print(data.json())
            print('#'*10)


def enviar_mensagem(chat_id, text, disable_notification=False):
    token = '5790788365:AAHA0RU0YkD8Ywuwfem1D8RDy7PftroNWeU'
    data = requests.get(
        f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}&disable_notification={disable_notification}')
    print(data.json())

def enviar_imagem(links_imagens,chat_id,caption):
    token = '5790788365:AAHA0RU0YkD8Ywuwfem1D8RDy7PftroNWeU'
    for link in links_imagens:
        requests.get(f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&photo={link}&caption={caption}')
        

# while True:
#     obter_mensagens(apenas_ultima_mensagem=False)
# enviar_mensagem(chat_id='-646901742',
#                 text='Compre agora este celular! https:www.celular.com', disable_notification=True)
imagens = ['https://i.ibb.co/D8hkPhj/foto-1.jpg','https://i.ibb.co/GQ1TT27/foto-2.jpg']
enviar_imagem(links_imagens=imagens,chat_id='-646901742',caption='Programador!')
# https://i.ibb.co/D8hkPhj/foto-1.jpg
# https://i.ibb.co/GQ1TT27/foto-2.jpg