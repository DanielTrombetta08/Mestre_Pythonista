from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler, CallbackQueryHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
import logging
from datetime import datetime

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Fluxo de criação para bot que responde a comandos:
# criar um função que faz algo quando um X comando é digitado


async def iniciar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    horario_atual = datetime.now().strftime('%H:%M:%S')
    keyboard = [
        [
            InlineKeyboardButton("Vagas Restantes",callback_data="Restam 10 vagas"),
            InlineKeyboardButton("Horário atual",callback_data=f"O horário atual é {horario_atual}")
        ],
        [
            InlineKeyboardButton("Sair",callback_data="Você escolheu sair")
        ],
        [
            InlineKeyboardButton('Exibir ano atual',callback_data=f'O ano atual é: {datetime.now().year}')
        ]
    ]

    reply_keyboard = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Favor selecionar uma opção:',reply_markup=reply_keyboard)

async def monitorador_de_respostas(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f'Opção escolhida: {query.data}')

async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Para começar a usar o bot, digite /iniciar ou /start')
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
        '5812917886:AAGw4I2hT2T79R6tTty9uCMqEm3gFzFbhX0').build()
    # registrar um handler de comandos(classe que observa se X comando foi digitado)
    application.add_handler(CommandHandler('iniciar', iniciar))
    application.add_handler(CommandHandler('start', iniciar))
    application.add_handler(CommandHandler('horas', horas))
    application.add_handler(CommandHandler('ajuda',ajuda))
    application.add_handler(CallbackQueryHandler(monitorador_de_respostas))
    application.add_handler(MessageHandler(filters.COMMAND, nao_registrado))
    application.add_handler(MessageHandler(filters.TEXT, responder))
    # "ligar" o monitaramento de comandos
    application.run_polling()