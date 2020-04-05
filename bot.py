# -*- coding: utf-8 -*-
import telebot
token = '1209038083:AAHASTtRKVTTkqaLR9GeNQcXNMWTBZcNiKM'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()