import smtplib
from email.message import EmailMessage
from time import sleep
import imghdr


class Emailer:
    def __init__(self, email_origem, senha_email):
        self.email_origem = email_origem
        self.senha_email = senha_email

    def definir_conteudo(self, topico, email_remetente, lista_contatos, conteudo_email):
        self.mail = EmailMessage()
        self.mail['Subject'] = topico
        mensagem = conteudo_email
        self.mail['From'] = email_remetente
        self.mail['To'] = ', '.join(lista_contatos)
        self.mail.add_header('Content-Type', 'text/html')
        self.mail.set_payload(mensagem.encode('utf-8'))

    def anexar_imagem(self, lista_imagens):
        for imagem in lista_imagens:
            with open(imagem, 'rb') as arquivo:
                dados = arquivo.read()
                extensao_imagem = imghdr.what(arquivo.name)
                nome_arquivo = arquivo.name
            self.mail.add_attachment(dados, maintype='image',
                                     subtype=extensao_imagem, filename=nome_arquivo)

    def anexar_arquivos(self, lista_arquivos):
        for arquivo in lista_arquivos:
            with open(arquivo, 'rb') as a:
                dados = a.read()
                nome_arquivo = a.name
            self.mail.add_attachment(dados, maintype='application',
                                     subtype='octet-stream', filename=nome_arquivo)

    def enviar_email(self, intervalo_em_segundos):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(user=self.email_origem, password=self.senha_email)
            smtp.send_message(self.mail)
            sleep(intervalo_em_segundos)
