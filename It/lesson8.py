# d = {}
# d['name'] = 'John Doe'
# d['age'] = 20

# for item in d.keys():
#     print(item)
# for item in d.items():
#     print(item)
# for item in d.values():
#     print(item)

# d.pop("age")
# print(d)
# print(d.popitem())
# print(d.clear())
# d.update({'salary': 300})
# print(d)

# keys = "abc"
# values = [1, 2, 3, 4]
# d = {k: v for (k, v) in zip(keys, values)}

# print(d)

# Task 4
# import random
# from faker import Faker   
# fake = Faker()
# users = {}
# for i in range(30):
#     name = fake.name()
#     f_name = {
#         f'{name.split(" ")[0].lower()}': random.randint(10,50)
#     }
#     users.update(f_name)
# print(users)

# Task 6
# for i in range(1):
#     user = input('write = ')
#     if len(user) > 3 and len(user) <=10:
#         arr = user.split('.')
#         # print(arr)
#         if arr[0] > '0' and arr[0] <'12':
#             if arr[1] > '0' and arr[1] < '31':
#                 if arr[2] > '1970' and arr[2] < '2023':
#                     print(arr)
#         else:
#             print(False)

# Task 8
# user = input('..')


# print(f'{int(user[0:2])-15}')
