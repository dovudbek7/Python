# Ternary
# x = 10
# print('yes') if x > 5 else print('no')
# print("yes" if 10 % 2 == 0 else "No")

# Loops
# For while
# While - to'xtovsiz sikl
# for - sanoqlli sikl

# for sikli - ketma ketliklar bilan ishlaydi
# for i in "python":
#     print(i)

# for i in range(5, 10):
#     print(i)

# print(type(range(5, 10)))
# print(dir(range(5, 10)))


# start = 1
# step = 3
# stop = 15
# for i in range(start, stop, step):
#     print(i)

# for x in range(10):
#     print(x)

# for k in 'stars':
#     print(type(k))
#     print(k)

# for i in input():
#     if i == 'a':
#         print("yes")

# def main(num):
#     return num ** num

# for x in range(10):print(main(x))

# enumerate - element va uni har  indexini olish uchun ishlatiladi
# s = " Python is n1"
# for i in enumerate(s):
# print(i)


# for i in range(5):
#     if i % 2 == 0:
#         print(i)
# else: # sikl tugasa biror ish qilish uchun else blokidan foydalaning
# print("loop tugadi")


# while False:
#     print('while')

# i = 0

# while True:
#     i += 1
#     if i % 10000000 == 0:
#         print('Nazrulloh Krisa')


# control = True
# while True:
#     u = input()
#     if u == '1234':
#         break #  bu siklni majburiy to'xtatish
#     else:
#         print("wrong")
#         continue # keyingi siklga o'tish
#     print("try again")


# Task 1
# count = 0
# while True:
#     num = input("Write.. ")
#     if num == "stop":
#         break
#     else:
#         num = int(num)
#         count += num
# print(count)

# Task 2
# alpha = 'abcdef'
# user = input('harfni kiriting  ')
# for letter in enumerate(alpha):
#     if user == letter[1]:
#         print(letter[0]+1, letter[1])


# count = 0
# while True:
#     user = int(input('sonni kiriting:  '))
    
#     if user >= len(2) :
#         continue
#     else:
#         print('xato')
# print(count)
