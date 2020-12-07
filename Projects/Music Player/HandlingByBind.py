import tkinter as tk


# bind method has 2 positinal argument
# 1 st string(name of event)
# 2 nd name of function that handle this event that is parameterised function
def changeC1(e):
    root.config(bg="red")


def changeC2(e):
    root.config(bg="blue")


root = tk.Tk()
root.geometry('300x300')
b1 = tk.Button(root, text="Red")
b1.pack()
b1.bind("<Button-1>", changeC1)
b1.bind("Button-3>", lambda e: root.config(bg="blue"))

root.mainloop()
