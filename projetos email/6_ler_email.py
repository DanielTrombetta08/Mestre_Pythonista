from imapclient import IMAPClient
from datetime import datetime, date
import email
from rich import print

# Configurações de login
HOST = 'imap.gmail.com'
USERNAME = 'daniel.trombetta.desenv@gmail.com'
PASSWORD = 'hajphavwmoitlvsb'
# Abrir conexão com servidor gmail
with IMAPClient(HOST) as server:
    server.login(USERNAME, PASSWORD)
    print(server.list_folders())
    server.select_folder('INBOX', readonly=True)
    # Pesquisa
    messages = server.search(
        [u'SINCE', date(datetime.now().year, datetime.now().month, datetime.now().day)])
    
    for uid, message_data in server.fetch(messages,'RFC822').items():
        email_message = email.message_from_bytes(message_data[b'RFC822'])
        print(f'id: {uid}')
        print(f'FROM: {email_message.get("From")}')
        print(f'TÓPICO: {email_message.get("Subject")}')
        if email_message.is_multipart():
            for part in email_message.walk():
                if part.get_content_type() in ('text/plain','text/html'):
                    try:
                        print(part.get_payload(decode=True).decode())
                    except UnicodeDecodeError as erro:
                        print(part.get_payload(decode=True).decode('latin-1'))