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
VALUES(?, ?, ?, ?, ?, ?, ?)""",(newid, newname, newcategory, newunits, newprice, newunit, newcost))
    db.commit()
    sid.delete(0, END)
    sname.delete(0, END)
    scategory.delete(0, END)
    sunits.delete(0, END)
    sprice.delete(0, END)
    spackage.delete(0, END)
    scost.delete(0, END)
    sname.focus()
    
    
    
    
    
