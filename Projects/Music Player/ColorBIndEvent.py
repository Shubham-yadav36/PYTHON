import tkinter as tk


def changec(e):
    ch = e.char
    if ch == 'r':
        root.config(bg="red")
    elif ch == 'g':
        root.config(bg="green")
    elif ch == 'b':
        root.config(bg="blue")


root = tk.Tk()
old = root["bg"]
root.bind("<Key>",changec)
root.mainloop()
