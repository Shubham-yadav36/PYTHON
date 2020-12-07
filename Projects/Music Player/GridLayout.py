import tkinter

root = tkinter.Tk()
root.geometry('400x400+400+100')
# root.minsize(400,400)
lb = tkinter.Label(root,text=" Welcome to perl",bg="cyan",fg="black")
lb1 = tkinter.Label(root,text="python",bg="blue",fg="black")
lb2 = tkinter.Label(root,text="Welcome to Java",bg="white",fg="black")
lb3 = tkinter.Label(root,text="Welcome to Html",bg="pink",fg="black")

lb.grid(row=0,column=0)
lb1.grid(row=0,column=1,sticky=tkinter.E+tkinter.W)
lb2.grid(row=1,column=0)
lb3.grid(row=1,column=1)
root.mainloop()
