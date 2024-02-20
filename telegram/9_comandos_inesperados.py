from contextvars import Context
from email.message import Message
from re import T
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler
from telegram import Update
import logging
from datetime import datetime

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Fluxo de criação para bot que responde a comandos:
# criar um função que faz algo quando um X comando é digitado


async def iniciar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Bem vindo ao bot da Dev Aprender', reply_to_message_id=update.message.id)


async def horas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hora_atual = datetime.now().strftime('%H:%M:%S')
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Hora atual: {hora_atual}')


async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.lower() in ('olá', 'oi', 'bom dia', 'tudo bem?', 'tudo bem'):
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Olá seja bem vindo a este atendimento!', reply_to_message_id=update.message.id)
    elif update.message.text.lower() in ('horários', 'horario', 'agendar', 'agendamento', 'agenda', 'marcar'):
        agenda = '''
        horário de funcionamento é das 08:00 as 19:00 de segunda a sexta
        '''
        await context.bot.send_message(chat_id=update.effective_chat.id, text=agenda, reply_to_message_id=update.message.id)


async def nao_registrado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Esse comando não é válido')


if __name__ == '__main__':
    application = ApplicationBuilder().token(
        '5795313128:AAHy2nIUSLbxVVEb6Sv-adRipJOYdrUb4K8').build()
    # registrar um handler de comandos(classe que observa se X comando foi digitado)
    application.add_handler(CommandHandler('iniciar', iniciar))
    application.add_handler(CommandHandler('horas', horas))
    application.add_handler(MessageHandler(filters.COMMAND, nao_registrado))
    application.add_handler(MessageHandler(filters.TEXT, responder))
    # "ligar" o monitaramento de comandos
    application.run_polling()