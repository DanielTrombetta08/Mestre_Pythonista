# TOKEN 6987893098:AAGXC_KZrsRVMm7USckQa2xzdrZb_RJICN0
# URL do API - https://api.telegram.org/bot6987893098:AAGXC_KZrsRVMm7USckQa2xzdrZb_RJICN0/getUpdates
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
    token = '6987893098:AAGXC_KZrsRVMm7USckQa2xzdrZb_RJICN0'
    data = requests.get(
        f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}&disable_notification={disable_notification}')
    print(data.json())


# while True:
#     obter_mensagens(apenas_ultima_mensagem=False)
enviar_mensagem(chat_id='-646901742',
                text='Compre agora este celular! https:www.celular.com', disable_notification=True)