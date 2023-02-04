# # pip -m pip install --upgrade pip
# # import colorama
# # print()




#     # all_links = persering.findAll('a')
#     # for i in all_links:
#     #     print('https://pyblog.uz/'+link['href'])
#     #     print(link.text)
    
    
# import requests
# import wget
# from bs4 import BeautifulSoup as bs
# url = 'https://pyblog.uz'

# page = requests.get(url=url)
# print(page.status_code)

# if page.status_code == 200:
#     persering = bs(page.text, 'html.parser')
#     images  = persering.findAll("img")
#     for i in images:
#         wget.download('https://pyblog.uz'+i["src"])
# else:
#     print('Not Founded')