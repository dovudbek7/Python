
# print("Python".lower())
# print("Python".swapcase())
# print("Python".capitalize())
# print("Python is better".title())
# print("Python is better".find("is")) #7
# print("Python is better".rfind("b")) #10
# print("Python is better".index("is")) #7
# print("on table non table".count("on")) #2
# print("aloha chicas".replace("chicas", "muchachos"))
# # print("Python is better".index("qq")) #ValueError: substring not found
# print("gandi".startswith("gan")) # True
# print("gandi".endswith("gan")) # False

""" isalnum () - stringda raqam borligini tekshirib beradi True False qaytaradi
"0123" . isalnum(), "123abc" . isalnum () , "abcl23" . isalnum()
(True, True, True)
» > "строка" . isalnum ()"""

"""" isalpha () — Stringdi tekshiradi
"string" .isalpha (), "строка" .isalpha (), "". isalpha ()
(True, True, False)
"""

"""" isdigit () - raqamdi o'zini tekshiradi 
"0123" . isdigit (), "123abc" . isdigit () , "abcl23" . isdigit ()
(True, False, False)
"""

""" isdecimal () -
"123" . isdecimal () , "123стр" . isdecimal ()
(True, False)
"""
""" isnumeric () - 
"\u2155" . isnumeric () , "\u2155" . isdigit ()
(True, False)
 print ("\u2155") # Выведет символ "1/5"""

""" isupper () — String faqat katta harflarda bo'lsa True qaytaradi
"STRING" . isupper () , "СТРОКА" . isupper () , isupper ()
(True, True, False)
 » "STRING1". isupper (), "СТРОКА, 123" . isupper () , "123" . isupper ()
(True, True, False)
 "string" . isupper () , "STRing" . isupper ()
(False, False)"""

"""" is lower () —  String faqat kichkina harf bo'lsa True qaytaradi
"srting" . islower () , "строка" . islower () , "" . islower ()
(True, True, False)
"stringl" . islower () , "str, 123" . islower () , "123" . islower ()
(True, True, False)
"STRING" . islower () , "Строка" . islower ()
(False, False)"""

"""istitie () — Bosh harfi katta bo'lsa True qaytaradi 
"Str Str" . istitie () , "Стр Стр" . istitie ()
(True, True)
"Str Str 123" . istitie (), "Стр Стр 123" . istitie ()
(True, True)
"Str str" . istitie () , "Стр стр" . istitie ()
(False, False)
”".istitie(), "123".istitie ()
(False, False)"""

""" isprintable () — Faqat chop etiladigan ishoralar bo'lsa Tru qaytaradi
"123" . isprintable {)
True
" РНР Python" . isprintable ()
True
"\n” . isprintable ()
False"""