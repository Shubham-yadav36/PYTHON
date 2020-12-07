import sys
import tkinter as tk


def show():
    fname = nf.get()
    lname = pf.get()
    tf.delete(0,tk.END)
    tf.insert(0,fname+" "+lname)


root = tk.Tk()
root.geometry('400x400+450+200')
name = tk.Label(root, text="First Name", fg="red")
nf = tk.Entry(root)
password = tk.Label(root, text="Last Name", fg="red")
pf = tk.Entry(root)
lf = tk.Label(root, text="You Type", fg="red")
tf = tk.Entry(root)
cb = tk.Label(root)
lb = tk.Button(root, text="Login", command=show)
qb = tk.Button(root, text="Quit", command=lambda: root.destroy())

name.grid(row=0, column=0, sticky=tk.W)
nf.grid(row=0, column=1, columnspan=2)

password.grid(row=1, column=0, sticky=tk.W)
pf.grid(row=1, column=1, columnspan=2)
tf.grid(row=2, column=1, columnspan=2)
lf.grid(row=2, column=0)

lb.grid(row=3, column=1, sticky=tk.W + tk.E)
qb.grid(row=3, column=2, sticky=tk.W + tk.E)

root.mainloop()
