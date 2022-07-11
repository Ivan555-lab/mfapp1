from tkinter import *

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






window.mainloop()
db.close()

                
                

                
