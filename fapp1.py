
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
VALUES("2", "Горох колотый", "Бакалея", "гр.", "35.99", "1000", "3.59")""")
db.commit()
db.close()   
