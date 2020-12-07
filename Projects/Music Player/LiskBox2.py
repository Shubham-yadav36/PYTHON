from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser, simpledialog


def show(e):
    item = lb.curselection()
    lb1.config(text="Selected :" + str(lb.get(item[0])))


root = Tk()
root.geometry('300x300')
lb = Listbox(root)
sp = ["cricket", 'Hocky', 'khokho', 'tenis', 'snooker', 'rugby']
for s in sp:
    lb.insert(END, s)

lb1 = Label(root,text="You Selected")
# lb.bind("<<ListboxSelect>>",show)
lb.bind("<<Double-click-1>>",show)

lb.pack()
lb1.pack()
root.mainloop()
