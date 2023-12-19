import smtplib
from email.message import EmailMessage

# Configurações de login
EMAIL_ADDRESS = 'daniel.trombetta.desenv@gmail.com'
EMAIL_PASSWORD = 'hajphavwmoitlvsb'

# Criar e enviar um email
mail = EmailMessage()
mail['Subject'] = 'Seu pacote chegou no correios'
mensagem = '''
Olá seu pacote acaba de chegar no correios, favor ir buscar até amanhã
Seu código de rastreio é XVB155125C2
'''
mail['From'] = EMAIL_ADDRESS
mail['To'] = 'danieltrombetta08@hotmail.com'
mail.add_header('Content-Type','text/html')
mail.set_payload(mensagem.encode('utf-8'))

# Enviar o email
with smtplib.SMTP_SSL('smtp.gmail.com',465) as email:
    email.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    email.send_message(mail)