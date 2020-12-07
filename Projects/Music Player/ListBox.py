from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser, simpledialog


def show():
    item = lb.curselection()
    if len(item) == 0:
        lb1.config(text="not Selected")
    else:
        lb1.config(text="Selected :" + str(lb.get(item[0])))


root = Tk()
root.geometry('300x300')
lb = Listbox(root)
sp = ["cricket", 'Hocky', 'khokho', 'tenis', 'snooker', 'rugby']
for s in sp:
    lb.insert(END, s)

lb1 = Label(root,text="You Selected")
bt = Button(root, text="Submit", command=show)

lb.pack()
bt.pack()
lb1.pack()
root.mainloop()
