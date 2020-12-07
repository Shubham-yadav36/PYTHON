from tkinter import *
from tkinter import colorchooser


def show():
    root.config(col.get())


root = Tk()
root.geometry('200x200')
col = StringVar()
btn = Checkbutton(root, text='Red', variable=col,command=show)
btn.deselect()
# btn = Checkbutton(root, text='Red', variable=c, command=show)

btn.pack()
root.mainloop()
