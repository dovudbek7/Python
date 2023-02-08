import requests


from bs4 import BeautifulSoup as bs

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

from telepot import Bot

bot = Bot(token='6180527513:AAFiPaEjN0mJNapMokQPAb-E46JXMdAuNQI')


g_id = 5594897676

# bot.sendMassage(g_id,'hello')
# print(bot.se(g_id,'hello'))
# jokes = None

while True:
    bot.sendMessage(g_id, 'aaa')

