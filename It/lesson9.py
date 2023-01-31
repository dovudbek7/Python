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

