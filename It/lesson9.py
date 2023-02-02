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
# from faker import Faker
# import random
# import math

# f = Faker()

# arr = []
# ob = {}
# for i in range(12):
#     salary = random.randrange(1000000, 15000000,1000000)
#     print(salary)
#     users = f.name()
#     pr = salary * 5 // 100 
#     for m in range(random.randint(1, 6)):
#         salary += pr
#         plus = salary
#     for w in range(random.randint(1,6)):
#         salary -= pr
#         minus = salary
#     year = (salary * 12) + (m * pr) - (w * pr)
#     kv = year // 4
#     d = {users : year}
#     ob.update(d)
#     arr.append(year)
#     print(f'Har bir ishchini 12 oyda olgan umumiy ish haqi summasi {users} : {year}')
#     print(f'Har bir ishchini kvartallar boyicha ish haqlari {users} : {kv}')
# arr.sort()   
# max_salary = arr[-1]
# z = list(ob.keys())[list(ob.values()).index(max_salary)]
# min_salary = arr[0]
# x = list(ob.keys())[list(ob.values()).index(min_salary)]
# print(f'yil davomida eng kop maosh olgan ishchin {z} {max_salary}')
# print(f'yil davomida eng kam maosh olgan ishchin {x} {min_salary}')
# print(f' eng kop maosh olgan ishchini eng kam olgan ortasidagi farq {max_salary - min_salary}')1


