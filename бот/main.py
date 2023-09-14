import telebot
from telebot import types
import config

bot=telebot.TeleBot(config.token)

@bot.message_handler(commands=['number'])
def phone(message):
    keyboard=types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone=types.KeyboardButton(text='Send phone', request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, 'номер отправителя', reply_markup=keyboard)

@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.cotact is not None:
        print(message.cotact)

print('bot started')
bot.polling()
