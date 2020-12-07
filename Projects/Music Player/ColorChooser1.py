from tkinter import *
from tkinter import colorchooser


def show():
    col = colorchooser.askcolor(color='#f1f1f1', title="Select a color")
    root.config(bg=col[1])
    print(col[1])


root = Tk()
root.geometry('200x200')
btn = Button(root, text="Click Me", command=show)
btn.pack()
root.mainloop()
