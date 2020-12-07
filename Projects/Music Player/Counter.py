import tkinter as tk

i = 0;


def countI():
    global i
    i = i + 1
    lb.config(text=f"{i}")


root = tk.Tk()
root.geometry('300x300')
b1 = tk.Button(root, text="Click Me", command=countI)
lb = tk.Label(root, text="0")
b1.pack()
lb.pack()
root.mainloop()
