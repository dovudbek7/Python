import requests
import wget
from bs4 import BeautifulSoup 

# url = "http://jsonplaceholder.typicode.com/users"

# data = requests.get(url=url)
# # print(data.json())
# names = []
# for i  in data.json():
#     if i["name"]:
#         names.append(["name"])

# print(names)


url = 'https://obhavo.uz/andijan'
r = requests.get(url)
pars = BeautifulSoup(r.text, 'html.parser')
t = pars.find_all('span', class_='forecast-day')
for i in t:
    print(i.text)
