import sqlite3
from tkinter import *

def addtolist():
    newid = sid.get()
    newname = sname.get()
    newcategory = scategory.get()
    newunits = sunits.get()
    newprice = sprice.get()
    newpackage = spackage.get()
    newcost = scost.get()
    cursor.execute("""INSERT INTO comp (id, Name, Category, Units, Price, Package, Cost)
VALUES(?, ?, ?, ?, ?, ?, ?)""",(newid, newname, newcategory, newunit, newprice, newunit, newcost))

