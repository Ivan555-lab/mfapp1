#it is place for dev
#f28_1  next1
#f28_2 start of dev 


import sqlite3

with sqlite3.connect("fapp1.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS comp(
  id integer PRIMARY KEY,
  Name text NOT NULL,
  Category text NOT NULL,
  Units text NOT NULL,
  Price of pack text NOT NULL,
  Package, gr. integer,
  Cost of 1 gram, decimal);""")
  



    
