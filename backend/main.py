import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN_BOT = os.getenv('TOKEN_BOT')

bot = telebot.TeleBot(TOKEN_BOT)
bot.set_my_commands([
    telebot.types.BotCommand("/start", "Menu principal"),
    telebot.types.BotCommand("/noticias", "Últimas notícias"),
    telebot.types.BotCommand("/gritar", "Simular torcida"),
    telebot.types.BotCommand("/quizz", "Responder quiz"),
    telebot.types.BotCommand("/ajuda", "Ver todos os comandos"),
])

@bot.message_handler(['start'])
def start(msg: telebot.types.Message):
    markup = types.InlineKeyboardMarkup()

    botao_jogos= types.InlineKeyboardButton('Próximos Jogos',callback_data='jogos')
    botao_ranking = types.InlineKeyboardButton('Ranking da FURIA', callback_data='ranking')

    markup.add(botao_jogos, botao_ranking)

    bot.send_message(msg.chat.id, 'Bem-vindo, fã da FURIA CS! O que você quer fazer?', reply_markup=markup)

@bot.message_handler(commands=['noticias'])
def noticias(msg):
    bot.send_message(msg.chat.id, "Últimas notícias: MIBR anuncia nova patrocinadora: LG UltraGear.")

# Simulador de Torcida
@bot.message_handler(commands=['gritar'])
def gritar(msg):
    bot.send_message(msg.chat.id, "FURIAAAAAAA!! 🔥🔥🔥 Vamos FURIA!")

@bot.message_handler(commands=['ajuda', 'help'])
def ajuda(msg):
    comandos = """
    🤖 *Comandos disponíveis*:

        /start - Menu principal  
        /noticias - Ver últimas notícias  
        /gritar - Simular torcida 🔥  
        /quizz - Responder quiz da FURIA  
        /ajuda - Ver todos os comandos  
        """
    bot.send_message(msg.chat.id, comandos)

# Quizz da Torcida
@bot.message_handler(commands=['quizz'])
def quizz(msg):
    # sidde peu thinkcard
    markup = types.InlineKeyboardMarkup()

    botao_sidde= types.InlineKeyboardButton('a) Sidde',callback_data='sidde')
    botao_peu = types.InlineKeyboardButton('b) Peu', callback_data='peu')
    botao_thinkcard = types.InlineKeyboardButton('c) Thinkcard', callback_data='thinkcard')

    markup.add(botao_sidde,botao_peu,botao_thinkcard)
    bot.send_message(msg.chat.id, "Qual é o nome do coach da MIBR CS?", reply_markup=markup)

@bot.callback_query_handler()
def resposta_botao(call:types.CallbackQuery):
    match call.data:
        case 'jogos':
            bot.send_message(call.message.chat.id, 'MIBR jogará contra SAW em 22/04. Acompanhe ao vivo!')
        case 'ranking':
            bot.send_message(call.message.chat.id, 'A FURIA está no #17 do ranking mundial. Vamos com tudo!')
        case 'sidde':
            bot.send_message(call.message.chat.id, '✅ Você acertou!!')
        case 'peu'| 'thinkcard':
            bot.send_message(call.message.chat.id, '❌ Errou!! :( Tente de novo')

        

bot.infinity_polling()
