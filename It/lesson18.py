# Task 1

# all = [
#     ('John', 4.5, '3:30'),
#     ('Alica', 5, '5:30'),
#     ('Ann', 5.5, '3:00')
# ]
# all.sort(key=lambda x  :x[1], reverse=True)

# for player in all:
#     all.sort(key=lambda x:int(player[2].split(":")[0]))
#     all.sort(key=lambda x:int(player[2].split(":")[1]))

# print(all)

# Task 2
import random

boys = [
    ('John', 'male', random.randint(1, 170)),
    ('Xurshidbek', 'male', random.randint(1, 170)),
    ('Nazrulloh', 'male', random.randint(1, 170))
]
girls = [
    ('Ann', 'female', random.randint(1, 170)),
    ('Sara', 'female', random.randint(1, 170)),
    ('Xurshidbek', 'female', random.randint(1, 170))
]
arr = []
boys.sort(key=lambda x  :x[2], reverse=True)
girls.sort(key=lambda x  :x[2], reverse=True)
for i in range(3):
    arr.append(boys[i])
    arr.append(girls[i])
print(arr)