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

label3 = Label(text = "Enter component category: ")
label3.place(x = 30, y = 125)
scategory = Entry(text = "")
scategory.place(x = 180, y = 125, width = 200, height = 25)
scategory.focus()




window.mainloop()
db.close()

                
                

                
