import tkinter

root = tkinter.Tk()
root.minsize(400,400)
lb = tkinter.Label(root,text="Welcome",bg="cyan")
lb1 = tkinter.Label(root,text="Welcome",bg="blue")
# lb.pack(fill=tkinter.X,padx=10)
# lb.pack(fill=tkinter.X,padx=(10,0))

# margin
lb.pack(fill=tkinter.X,padx=(10,20))
lb1.pack(fill=tkinter.X,pady=(10,20))

# padding

lb.pack(fill=tkinter.X,ipadx=20,side=tkinter.RIGHT)
lb1.pack(fill=tkinter.X,ipady=30,side=tkinter.RIGHT)
root.mainloop()
