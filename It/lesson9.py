# import time
# import datetime
# import calendar
# import locale

# time
# print(time.time()) #1970-1-01 > now() ? qancha sekund
# print(dir(time))

# now = datetime.datetime.now()
# print(now)
# print(type(now))
# print(dir(now))


# day = now.day
# month = now.month
# year = now.year
# print(day)
# print(month)
# print(year)


# user =input( ' yil oy kun ')
# splits = user.split(' ')
# now = datetime.datetime.now()
# year = now.year
# month = now.month


# print((year - splits[0]), (month - splits[1]))
    
# from timeit import Timer


# code = """/
# i = 1
# while = i <10**2:
#     i = i + 1

# """
# t = Timer(stmt=code)
# print("while : \n", t.timeit(number=1000))
# from timeit import Timer

# code = """\
# i = 1
# while i < 10**5:
#     i = i+1
# """
# t = Timer(stmt=code)
# print("While : \n", t.timeit(number=1000))


# Task 7
# 12 ta ishchi ism familyasini Faker orqali hosil qiling
# har bir ishchi 12 oy davomida (1 yil) har bir oyda ma'lum bir miqdorda oylik maosh olgan
# oylik maoshlar stabil oylik maosh summasidan ishchini ishlashiga qarab ayrim oylarda +5% ko'proq , ayrim oylarda -5% kamroq bo'lishi mumkin. Siz ushbu malumotlardan foydalanib hisoblashingiz kerak. 
# 1-Har bir ishchini 12 oyda olgan umumiy ish haqi summasi 
# 2- Har bir ishchini kvartallar boyicha ish haqlarini 
# 3- yil davomida eng ko'p maosh olgan ishchini 
# 4- yil davomida eng kam moash olgan ishchini 
# 5- eng kop maosh olgan ishchini eng kam olgan  bilan oyliklari o'rtasidagi farqni



# import random
# from faker import Faker

# fake = Faker()

# worker = []
# monthly = [[],[],[],[],[],[],[],[],[],[],[],[],]

# for i in range(12):
#     name = fake.name()
#     worker.append(name)
# index_arr = -1
# for k in range(156):
#     if k == 12 or k == 24 or k == 36 or k == 48 or k == 60 or k == 72 or k == 84 or k == 96 or k == 108 or k == 120 or k == 132 or k == 144 or k == 156 :
#         index_arr += 1
#         for x in range(12):
#             random_monthliy = random.randint(1000 , 7000)
#             random_multiplier = random.randint(0 , 1)
#             if random_multiplier == 0:
#                 random_monthliy - (random_monthliy * 0.5)
#             else:
#                 random_monthliy + (random_monthliy * 0.5)
#             monthly[index_arr].append(random_monthliy)

# worker_list = {}
# for i in range(12):
#     worker_list.update({worker[i]:sum(monthly[i])})
# # print(f"barcha ishchilar yilligi:\n{worker_list}")
# first_index = -1
# second_index = 0
# third_index = -3
# for i in range(48):
#     if i == 4 or i == 8 or i == 12 or i == 16 or i == 20 or i == 24 or i == 28 or i == 32 or i == 36 or i == 40 or i == 44 or i == 48:
#         first_index = first_index + 1
#         for a in range(4):
#             # print(sum(monthly[first_index][third_index : second_index]))
#             second_index = second_index + 3
#             third_index = third_index + 3
#             print(monthly[first_index][3:6])
#             print(monthly[index_arr])



# Task 7
from faker import Faker
import random
fake = Faker()
for i in range(12):
    workers_name = fake.name()
    print(workers_name)

for y in range(12):
    months = random.randint(1000, 7000)
    months_round = round(months)
    print(months)
# alpha = "abcdefgh"
# print(list(zip(alpha, list(range(len(alpha))))))
# [('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4), ('f', 5), ('g', 6), ('h', 7)]
# letters = list(zip(alpha, list(range(len(alpha)))))