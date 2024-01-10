from email_sender import Emailer


contatos = ['daniel.trombetta.desenv@gmail.com','danieltrombetta08@hotmail.com']
mail = Emailer('daniel.trombetta.desenv@gmail.com', 'hajphavwmoitlvsb')
mail.definir_conteudo('Tópico 1', 'daniel.trombetta.desenv@gmail.com',contatos,'Olá, seja bem vindo')
mail.enviar_email(10)
