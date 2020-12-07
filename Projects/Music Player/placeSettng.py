import tkinter

root = tkinter.Tk()
root.minsize(400,400)
lb = tkinter.Label(root,text="Welcome",bg="cyan")
lb1 = tkinter.Label(root,text="Welcome",bg="blue")

lb.place(x=20,y=40)
lb1.place(x=20,y=300)
root.mainloop()
