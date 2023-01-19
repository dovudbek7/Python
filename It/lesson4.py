# print(int('1.2')+2)
# print(float('1.2')+2)
# print(float(1)+2.2)

# bin
# print(bin(10)) # 0b1010
# print(oct(10)) # 0o12
# print(hex(10)) # 0xa


# print(round(12.2)) # 12
# print(round(12.6)) # 13

# print(abs(-12))  # 12
# print(pow(2, 6))  # 64

# print(min([1, 2, 3]))  # 1
# print(max([1, 2, 3]))  # 3
# print(sum([1, 2, 3]))  # 6

# n = 10.0
# n1 = 10.3
# print(n.is_integer())
# print(n1.is_integer())


# variant 1
# import math
# print(math.pi) # 3.141592653589793
# # variant 2
# from math import pi
# print(pi) # 3.141592653589793

# import math

# print(math.ceil(12.6))  # 13
# print(round(12.6))  # 13
# print(math.floor(12.6))  # 12

# import random
# print(round(random.random() * 4)) # 0 va kiritlgan son orasidagi tasodifiy son
# print(random.Random())
# print(random.randint(0, 10)) # 2 ta son orasidagi tasodifiy son


# import random
# ketma-ketlikdan tasodifiy bitta elementni olish
# import random
# print(random.choice('python'))
# # ketma-ketlikdan tasodifiy bir nechta  elementni olish
# print(random.sample('python', 6))
# arr = [1, 2, 3, 4, 5]  # berilgan massiv  elementlarini indexlarini qorishtirish
# random.shuffle(arr)
# print(arr)

import random
# Task 1
# letter_low = 'qwertyuiopasdfghjklzxcvbnm'
# letter_up = letter_low.upper()
# symblos = '!@#$%^&*()'

# chars = letter_low + letter_up + symblos
# pass_count = int(input('Count ? \n'))
# letter_count = int(input("Letter count ? \n"))

# if letter_count >= 6:
#     for i in range(pass_count):
#         password = ''
#         for l in range(letter_count):
#             password += random.choice(chars)
#         print(password)

# Task 2

# new = 'yangi o\'zbekiston'
# letter = 'svet'
# counter = 0

# for char in new:
#     for i in letter:
#         if char == i:
#             counter

# print(counter)
# print(len("".join([x for i in "svet" for x in 'yangi ozbekiston' if i == x])))

# user = range(1, 10)

# print(user)

for i in range(1, 10):
    print(i)
    