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

@bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.reply_to_message: #проверка на то, что эта команда была вызвана в ответ на сообщение 
        chat_id = message.chat.id # сохранение id чата
         # сохранение id и статуса пользователя, отправившего сообщение
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status 
         # проверка пользователя
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно забанить администратора.")
        else:
            bot.ban_chat_member(chat_id, user_id) # пользователь с user_id будет забанен в чате с chat_id
            bot.reply_to(message, f"Пользователь @{message.reply_to_message.from_user.username} был забанен.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите забанить.")

@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)
    
bot.infinity_polling()