from tkinter import *
from tkinter import colorchooser


# def show():
#     if col.get() == 1:
#         root.config(bg='red')
#     else:
#         root.config(bg="white")

def show():
    if col.get() == "Shubh":
        root.config(bg="blue")
    else:
        root.config(bg="pink")


root = Tk()
root.geometry('200x200')
# col = IntVar()
col = StringVar()
btn = Checkbutton(root, text='Red', variable=col,onval="Shubh",offval="Renu", command=show)
btn.deselect()
# btn = Checkbutton(root, text='Red', variable=c, command=show)

btn.pack()
root.mainloop()
