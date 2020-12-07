import tkinter as tk


root = tk.Tk()
root.geometry('300x300')
lb = tk.Label(root, height=3, width=20, bg="white")
b1 = tk.Button(root, text="Red", width=6, command=lambda : lb.config(bg="red"))
b2 = tk.Button(root, text="Green", width=6, command=lambda : lb.config(bg="green"))
b3 = tk.Button(root, text="Blue", width=6, command=lambda : lb.config(bg="blue"))

lb.grid(row=0, column=1)
b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)

root.mainloop()
