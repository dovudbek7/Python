# def func_name(arguments):

# function block
# return


# def main(x):

#     pass # hech qanday amal yo'q

# class main:
#     pass

# for i in range(10):
#     pass

# def func():

#     print("func")

#     return 'func 1'

# print(func)
# print(func())

# def jls_extract_def():

#     return


# def num(*args):
#     s = 0
#     for i in args:
#         s = s + 1
#     return round(s)
# print(num(1.1,5))


# main = lambda x : x +10
# print(main(10))


# def main(num):
#     if num % 2 == 0:
#         return print(lambda num: num ** 2)
#     else:
#         return lambda num: num - 2


# print(main(6)
from benchmark import banchmark


@banchmark(func)
def fetch_wabpage():
    import request
    webpage = request.get('https://google.com')
