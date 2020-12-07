import sys
import tkinter as tk
from tkinter import messagebox


class MyGuiApp:
    def __init__(self, root):
        self.root = root

        self.first = tk.Label(root, text="First Number", fg="red")
        self.f1 = tk.Entry(root)
        self.second = tk.Label(root, text="Second Number", fg="red")
        self.f2 = tk.Entry(root)
        self.Result = tk.Label(root, text="Result", fg="red")
        self.f3 = tk.Entry(root, fg="green")
        self.res = tk.Label(root, text="Result", fg="red")
        self.lb = tk.Button(root, text="Divide", command=self.divide)
        self.cl = tk.Button(root, text="Clear", command=self.clear)
        self.qb = tk.Button(root, text="Quit", command=lambda: root.destroy())

        self.first.grid(row=0, column=0, sticky=tk.W)
        self.f1.grid(row=0, column=1, columnspan=2)

        self.second.grid(row=1, column=0, sticky=tk.W)
        self.f2.grid(row=1, column=1, columnspan=2)

        self.res.grid(row=2, column=0, sticky=tk.W)
        self.f3.grid(row=2, column=1, columnspan=2)

        self.lb.grid(row=3, column=0, sticky=tk.W + tk.E)
        self.cl.grid(row=3, column=1, sticky=tk.W + tk.E)
        self.qb.grid(row=3, column=2, sticky=tk.W + tk.E)

    def show(self):
        self.fname = self.nf.get()
        self.lname = pf.get()
        self.tf.delete(0, tk.END)
        self.tf.insert(0, fname + " " + lname)

    def clear(self):
        self.f1.delete(0, tk.END)
        self.f2.delete(0, tk.END)
        self.f3.delete(0, tk.END)

    def divide(self):
        done = False
        self.f3.delete(0, tk.END)
        try:
            a = int(self.f1.get())
            b = int(self.f2.get())
            r = a / b
            self.f3.insert(0, str(r))
        except ZeroDivisionError:
            self.f3.config(fg="red")
            self.f3.delete(0, tk.END)
            self.f3.insert(0,"Divide By 0")


root = tk.Tk()
root.geometry('400x400+450+200')
mygui = MyGuiApp(root)
root.mainloop()
