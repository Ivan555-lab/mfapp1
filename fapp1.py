
#2

#1

import sqlite3

with sqlite3.connect("fapp1.db") as db:
    cursor = db.cursor()



cursor.execute("""INSERT INTO comp(id, Name, Category, Units, Price, Package, Cost)
VALUES("4", "Курятина", "Мясные", "гр.", "149.9", "1000", "14.99")""")
db.commit()

cursor.execute("""INSERT INTO comp(id, Name, Category, Units, Price, Package, Cost)
VALUES("5", "Кефир", "Молочные", "гр.", "30.9", "900", "3.43")""")
db.commit()
db.close()
