import tkinter as tk
import datetime

obj = datetime.datetime.now()
cdate = obj.strftime("%d-%b-%Y, %H.%M.%S %p")
print(cdate)


def printH():
    pmsg.config(text=f"{cdate}")


root = tk.Tk()
root.geometry('300x300')
b = tk.Button(root, text="Click Me", command=printH)
pmsg = tk.Label(root)
b.pack()
pmsg.pack()
root.mainloop()
