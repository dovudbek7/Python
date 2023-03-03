import random
from faker import Faker

f = Faker()
passed = []
nop = []
for i in range(10):
    students = f.name()
    all = []
    for b in range(3):
        point = random.randint(10, 33)
        all.append(point)
    s = sum(all)
    d = {students : s}
    print(d)
    if s >= 75:
        x = list(d.keys())[list(d.values()).index(s)]
        a = f'{x} : {s}'
        passed.append(a)
    else:
        m = list(d.keys())[list(d.values()).index(s)]
        b = f'{m} : {s}'
        nop.append(b)
    
print(passed)
print(nop)
