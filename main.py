import telebot
import config
#from telebot import types
#import random

dict={307035766: 'Сообщение от димы ',434043591: 'Сообщение от Оли'}

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start','help'])
def start (message):
   print (message.chat.id)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
   if message.from_user.id==307035766:
      bot.send_message(message.chat.id, 'от Димы ' + dict[message.from_user.id])
   if message.from_user.id==434043591:
      bot.send_message(message.chat.id, 'от Оли ' + dict[message.from_user.id])
   print('message.chat.id',str(message.chat.id)+" "+message.text)
   dict[message.chat.id]=message.text
   print('dict ',dict )
   print(dict[message.chat.id])
bot.polling()