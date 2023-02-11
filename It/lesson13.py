# import requests


# from bs4 import BeautifulSoup as bs

# url = "https://latifa.uz/"

# HEADER = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
# }

# page = requests.get(url=url, headers=HEADER)

# soup = bs(page.text, "html.parser")


# divs = soup.findAll('div', attrs={'data-id' : True})
# print(len(divs))
# arr = {}
# for i in divs:
#     arr.append(i.text)
#     # print(soup.text)
# print(arr)


# jokes = {}
# import json
# for i in divs:
#     jokes.update({f"{i[data-id]}:i.text"})
# with open("jokes.json", 'w+', encoding='utf-8') as file:
#     for k in jokes.items():
#         file.write(json.dumps(jokes))

# from telepot import Bot

# bot = Bot(token='6180527513:AAFiPaEjN0mJNapMokQPAb-E46JXMdAuNQI')


# g_id = 5594897676

# bot.sendMassage(g_id,'hello')
# print(bot.se(g_id,'hello'))
# jokes = None

# while True:
#     bot.sendMessage(g_id, 'aaa')

# import telebot


# bot_API = '6180527513:AAFiPaEjN0mJNapMokQPAb-E46JXMdAuNQI'

# bot = telebot.TeleBot(bot_API)
# @bot.message_handler(commands=['go'])
# def hello(message):
#     for i in range(100): 
#         bot.send_message(message.chat.id,'aaa')
# import telebot 
# print(dir(telebot))




# import time
# import telepot
# from telepot.loop import MessageLoop

# def handle(msg):
#     content_type, chat_type, chat_id = telepot.glance(msg)
#     print(content_type,chat_type, chat_id)
    
#     if content_type == 'text':
#         if msg['text'].lower() == 'salom':
#             bot.sendMessage(chat_id,salom)
#         else:
#             bot.sendMessage(chat_id,'Salom ber!')      

# bot.telepot.Bot(token='6180527513:AAFiPaEjN0mJNapMokQPAb-E46JXMdAuNQI')

# print('listening ... !')

# while 1:



# import asyncio
# import logging
# from aiogram import Bot, Dispatcher, types
import telebot

# logging.basicConfig(level=logging.INFO)

# bot = Bot(token="")

# import telebot
# from bs4 import BeautifulSoup as b

bot_API = '6180527513:AAFiPaEjN0mJNapMokQPAb-E46JXMdAuNQI'
bot = telebot.TeleBot(bot_API)

@bot.message_handler(['go'])
@bot.message_handler(content_types='text')
def h(mes):
    print(dir(mes))
    print(mes.date)
    print(mes.message_id)
    
    
    
bot.polling()
