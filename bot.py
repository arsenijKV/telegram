from config import token
from random import choice
import telebot

bot = telebot.TeleBot(token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Ну привет, мой маленький Егоиста")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
#@bot.message_handler(func=lambda message: True)
#def echo_message(message):
    #bot.reply_to(message, message.text)

@bot.message_handler(commands=['info'])
def about(message):
    bot.reply_to(message, """\
                 Я бот эгоист - сын недопрагромитса, должен тебе служить(я тебя сокрушу)
                 мои команды - egoist: покажет кто ты, вундеркинд или гений
                 fact - раскидываю факты\
""")

@bot.message_handler(commands=['egoist'])
def whoareyou(message):
    egoist = choice(["ВУНДЕРКИНД", "ГЕНИЙ"])
    bot.reply_to(message, egoist)


@bot.message_handler(commands=['fact'])
def fact(message):
    facts = choice(['Егоист - это тот кторый расщитывает только на себя','Поток - это полная концетрация направленая в одно дело',
                    'Вундеркинд - тот кто может донести и показать гениев миру','Гений - человек, который делает невероятное',
                    'Ыундеркинд и гений 2 стороны 1 монеты'])
    bot.reply_to(message, facts)

bot.infinity_polling()