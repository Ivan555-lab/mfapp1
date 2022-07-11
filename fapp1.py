
import sqlite3

with sqlite3.connect("fapp1.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS comp(
  id integer PRIMARY KEY,
  Name text NOT NULL,
  Category text NOT NULL,
  Units text NOT NULL,
  Price decimal NOT NULL,
  Package integer,
  Cost decimal);""")



  




cursor.execute("""INSERT INTO comp(id, Name, Category, Units, Price, Package, Cost)
VALUES("3", "Вермешель", "Бакалея", "гр.", "24.96", "450", "5,54")""")
db.commit()
db.close()
