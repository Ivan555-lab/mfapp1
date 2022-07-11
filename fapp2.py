from tkinter import *

window = Tk()
window.title("Comp")
window.geometry("450x400")

label1 = Label(text = "Enter component id: ")
label1.place(x = 30, y = 35)
sid = Entry(text="")
sid.place(x = 150, y = 35, width = 200, height = 25)
sid.focus()

label2 = Label(text = "Enter component name: ")
label2.place(x = 30, y = 80)
sname = Entry(text="")
sname.place(x = 150, y = 80, width = 200, height = 25)
sname.focus()

window.mainloop()
db.close()

                
                

                
