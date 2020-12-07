import sys
import tkinter as tk
from tkinter import messagebox


def show():
    fname = nf.get()
    lname = pf.get()
    tf.delete(0, tk.END)
    tf.insert(0, fname + " " + lname)


# Confirmation box
def finish():
    ans = messagebox.askyesno("Quit", "Are you sure ?")
    if ans:
        root.destroy()


def clear():
    f1.delete(0, tk.END)
    f2.delete(0, tk.END)
    f3.delete(0, tk.END)


def divide():
    done = False
    f3.delete(0, tk.END)
    try:
        a = int(f1.get())
        b = int(f2.get())
        r = a / b
        f3.insert(0, str(r))
    except ZeroDivisionError:
        f3.config(fg="red")
        # f3.delete(0, tk.END)
        # f3.insert(0,"Divide By 0")
        messagebox.showerror("Arightmetic Error", "Denominator Should not be Zero")
    except ValueError:
        f3.config(fg="red")
        # f3.delete(0, tk.END)
        # f3.insert(0,"Number is Allowed Only")
        messagebox.showerror("Value Error", "Value Should be Int")


root = tk.Tk()
root.geometry('400x400+450+200')
first = tk.Label(root, text="First Number", fg="red")
f1 = tk.Entry(root)
second = tk.Label(root, text="Second Number", fg="red")
f2 = tk.Entry(root)
Result = tk.Label(root, text="Result", fg="red")
f3 = tk.Entry(root, fg="green")
res = tk.Label(root, text="Result", fg="red")
lb = tk.Button(root, text="Divide", command=divide)
cl = tk.Button(root, text="Clear", command=clear)
qb = tk.Button(root, text="Quit", command=finish)

first.grid(row=0, column=0, sticky=tk.W)
f1.grid(row=0, column=1, columnspan=2)

second.grid(row=1, column=0, sticky=tk.W)
f2.grid(row=1, column=1, columnspan=2)

res.grid(row=2, column=0, sticky=tk.W)
f3.grid(row=2, column=1, columnspan=2)

lb.grid(row=3, column=0, sticky=tk.W + tk.E)
cl.grid(row=3, column=1, sticky=tk.W + tk.E)
qb.grid(row=3, column=2, sticky=tk.W + tk.E)

root.mainloop()
