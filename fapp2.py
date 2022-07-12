
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

def clearlist():
    sid.delete(0, END)
    sname.delete(0, END)
    scategory.delete(0, END)
    sunits.delete(0, END)
    sprice.delete(0, END)
    spackage.delete(0, END)
    scost.delete(0, END)
    sname.focus()

with sqlit3.connect("fapp1.db") as db:
    cursor = db.cursor()
    

window = Tk()
window.title("Comp")
window.geometry("450x400")

label1 = Label(text = "Enter component id: ")
label1.place(x = 30, y = 35)
sid = Entry(text="")
sid.place(x = 180, y = 35, width = 200, height = 25)
sid.focus()

label2 = Label(text = "Enter component name: ")
label2.place(x = 30, y = 80)
sname = Entry(text="")
sname.place(x = 180, y = 80, width = 200, height = 25)
sname.focus()

label3 = Label(text = "Enter  category: ")
label3.place(x = 30, y = 125)
scategory = Entry(text = "")
scategory.place(x = 180, y = 125, width = 200, height = 25)
scategory.focus()

label4 = Label(text = "Enter units: ")
label4.place(x = 30, y = 170)
sunits = Entry(text = "")
sunits.place(x = 180, y = 170, width = 200, height = 25)
sunits.focus()

label5 = Label(text = "Enter price: ")
label5.place(x = 30, y = 215)
sprice = Entry(text = "")
sprice.place(x = 180, y = 215, width = 200, height = 25)
sprice.focus()

label6 = Label(text = "Enter package: ")
label6.place(x = 30, y = 260)
spackage = Entry(text = "")
spackage.place(x = 180, y = 260, width = 200, height = 25)
spackage.focus()

label7 = Label(text = "Enter cost: ")
label7.place(x = 30, y = 305)
scost = Entry(text = "")
scost.place(x = 180, y = 305, width = 200, height = 25)
scost.focus()




window.mainloop()
db.close()

                
                

                

