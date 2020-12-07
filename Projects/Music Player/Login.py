import tkinter as tk

root = tk.Tk()
root.geometry('400x400+450+200')
name = tk.Label(root,text="Name",fg="red")
nf = tk.Entry(root)
password = tk.Label(root,text="Password",fg="red")
pf = tk.Entry(root)
cb = tk.Checkbutton(root,text="Keep me logged in")
lb = tk.Button(root,text="Login")
qb = tk.Button(root,text="Quit")

name.grid(row=0,column=0,sticky=tk.W)
nf.grid(row=0,column=1,columnspan=2)

password.grid(row=1,column=0,sticky=tk.W)
pf.grid(row=1,column=1,columnspan=2)
cb.grid(row=2,column=0,columnspan=2)
lb.grid(row=3,column=1,sticky=tk.W+tk.E)
qb.grid(row=3,column=2,sticky=tk.W+tk.E)

root.mainloop()