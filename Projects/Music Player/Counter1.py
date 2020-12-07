import tkinter as tk


def countI():
    obj.set(obj.get()+1)


root = tk.Tk()
root.geometry('300x300')
b1 = tk.Button(root, text="Click Me", command=countI)
obj = tk.IntVar()
lb = tk.Label(root, textvariable=obj)
b1.pack()
lb.pack()
root.mainloop()
