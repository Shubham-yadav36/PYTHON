from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser, simpledialog


def show():
    item = lb.curselection()

    if len(item) == 0:
        lb1.config(text="not Selected")
    else:
        sel = "\n"
        for i in item:
            sel += lb.get(i) + "\n"
        lb1.config(text="Selected :" + str(lb.get(sel)))


root = Tk()
root.geometry('300x300')
lb = Listbox(root, selectmod=MULTIPLE)
# lb = Listbox(root,selectmod=BROWSE)
sp = ["cricket", 'Hocky', 'khokho', 'tenis', 'snooker', 'rugby']
for s in sp:
    lb.insert(END, s)

lb1 = Label(root, text="You Selected")
bt = Button(root, text="Submit", command=show)

lb.pack()
bt.pack()
lb1.pack()
root.mainloop()
