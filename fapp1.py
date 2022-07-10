#it is place for dev
#f28_1  next1
#f28_2 start of dev
# next step of dev (step 3)
# step 4
# step5
# step6

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
VALUES("1", "Яйца", "яйца", "piece", "28.50", "1", "2.85")""")
db.commit()
db.close()
  



    
