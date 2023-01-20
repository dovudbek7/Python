# import calendar
# import locale
# locale.setlocale(locale=locale.LC_ALL, locale="uz_UZ.utf8")

# cal = calendar.LocaleHTMLCalendar()
# print(cal.formatmonth(theyear=2023, themonth=1))
# s = 'Python'

# print(s[0], s[1])  # p y
# print(s[6])  # IndexError: string index out of range

# num_str = str(123)
# print(num_str + 4)  # TypeError: can only concatenate str (not "int") to str
# print(num_str + '4')  # 1234

# print("symblo \n new line")
# print("symblo \t tab ")
# print("assalomu \n alaykum ")
# print(r"assalomu \n alaykum ") # assalomu \n alaykum
# print("assalomu \n alaykum ")
# s = "Bu 'qora' olma"
# s = 'bu "qora" olma'
# print(s)
# print(s[len(s)-1])

# s = "ruby on rails"
# on = s[0:5]
# print(on) # ruby
# print(len(on)) # 5
# print(s)

# print(s[:3])
# print(s[3:])
# print(s[:])  # string copy
# print('kitob'[::-1]) # botik

# age = 30
# name = 'John doe'

# user = 'name = %s, age = %s' % (name,  age)  # name = John doe, age = 30
# print(user)

# user = 'name = {0}, age = {1}'.format(name, age)  # name = John doe, age = 30
# print(user)

# # Python V3
# user = f'name = {name}, age = {age}'.format(name, age) # name = John doe, age = 30
# print(user)


# s = 'python string methods'
# print(s.center(50))

# print(ascii(p))

# s = " salom,xayr, qale"
# print(len(s))
# print(s.strip(" "))
# print(s.lstrip())
# print(s.rstrip())
# print(len(s.strip()))
# print(s.split(','))  # [' salom', 'xayr', ' qale']
#  assalomu alaykum bizda gaz svet yo\'q sizlarning Gazingiz bormi svetlaringchi
user = input('write.. ')
lower = user.lower()

g = lower.count('gaz')
s = lower.count('svet')
y = lower.count('yoq')
print(f'gaz = {g}')
print(f'svet = {s}')
print(f'yoq = {y}')
# print(lower.find('svet'))
