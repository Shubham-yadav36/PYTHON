import tkinter as tk


# bind method has 2 positinal argument
# 1 st string(name of event)
# 2 nd name of function that handle this event that is parameterised function
def changeC1(e):
    root.config(bg="red")


def changeC2(e):
    root.config(bg="blue")


root = tk.Tk()
old = root["bg"]
root.bind("<Return>",lambda e:root.config(bg="red"))
root.bind("<Escape>",lambda e:root.config(bg=f"{old}"))
root.mainloop()
