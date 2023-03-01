import sqlite3

# db ga ulanish obyekt
con = sqlite3.connect('./sql/firtst_db.db', check_same_thread=False)
cur = con.cursor()  # boshqarish obyekti

try:
    data = cur.execute(
        '''
    SELECT name,age , payment FROM students
    WHERE age>=16 AND payment='true'

    ''')
except sqlite3.DatabaseError as error:
    print(error)
else:
    print(data.fetchall())
