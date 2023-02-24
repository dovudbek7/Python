# from tkinter import *

# window = Tk() # yangi tkinter oyna obyelti
# window.title("Converter") # oyna sarlavhsai
# window.geometry('400x250') # oyna hajmi

# def convert_value():
#   value = entry.get()
#   lbl =Label(bg='#FAFAFA',text=f"{value} ", font=("Poppins SemBold", 16))
#   lbl.grid(column=0, row=1)
  
# entry = Entry(bg='#FAFAFA', font=("Poppins SemBold", 16))
# btn = Button(text="Convert", bg="#232323", foreground="#FAFAFA", font=("Poppins SemBold", 10), command=convert_value)

# entry.grid(column=0, row=0)
# btn.grid(column=1, row=0)

# window.mainloop()
# import response
# import requests





# import requests
# from aiogram import Bot, Dispatcher, executor, types

# API_TOKEN = ''

# # Initialize bot and dispatcher
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)


# def get_movie_poster(query:str):
#     url = "rapid url"

#     querystring = {"q":query}

#     headers = {
#         "X-RapidAPI-Key": "your key",
#         "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
#     }

#     response = requests.request("GET", url, headers=headers, params=querystring)
#     data = response.json()
#     url = data["d"][0]["i"]["imageUrl"]
#     return url

# @dp.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """
#     await message.reply("Hi!\nI'm MoviePosterBot!\nPowered by me.")



# @dp.message_handler()
# async def echo(message: types.Message):
#     # print(message.from_user)
#     url = get_movie_poster(message.text)
#     await message.answer(url)


# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)


# import time
# import telepot
# from telepot.loop import MessageLoop

# def handle(msg):
#     content_type, chat_type, chat_id = telepot.glance(msg)
#     # print(content_type, chat_type, chat_id)
    
#     if content_type == 'text':
#         if msg["text"].lower() == "salom":
#             bot.sendMessage(chat_id, "salom")
#         else:
#             bot.sendMessage(chat_id, "Salom ber !")

#  # get token from command-line

# bot = telepot.Bot(token="6145009119:AAExs6OT4pjlV-34sMCgRhvhB_Xi9SMlmJE")
# MessageLoop(bot, handle).run_as_thread()
# print ('Listening ...')

# Keep the program running.
# while 1:
#     time.sleep(10)


import random












# round1 =[]
# for i in range(4):
#     p = random.randint(1, 50)
#     round1.append(p)
# mx = max(round1)
# mn = min(round1)
# ortacha = (round1[0]+round1[1]+round1[2]+round1[3])/4
# print(f'First round {round1}')
# print(f'max : {mx}  min : {mn}  between : {ortacha}')




# round2 =[]
# for i in range(4):
#     p = random.randint(1, 50)
#     round2.append(p)
# mx = max(round2)
# mn = min(round2)
# ortacha = (round2[0]+round2[1]+round2[2]+round2[3])/4
# print(f'Second round {round2}')
# print(f'max : {mx}  min : {mn}  between : {ortacha}')

# round3 =[]
# for i in range(4):
#     p = random.randint(1, 50)
#     round3.append(p)
# mx = max(round3)
# mn = min(round3)
# ortacha = (round3[0]+round3[1]+round3[2]+round3[3])/4
# print(f'Third round {round3}')
# print(f'max : {mx}  min : {mn}  between : {ortacha}')

# round4 =[]
# for i in range(4):
#     p = random.randint(1, 50)
#     round4.append(p)
# mx = max(round4)
# mn = min(round4)
# ortacha = (round4[0]+round4[1]+round4[2]+round4[3])/4
# print(f'Fourth round {round4}')
# print(f'max : {mx}  min : {mn}  between : {ortacha}')
