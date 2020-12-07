import tkinter
import tkinter.font as tkf
root = tkinter.Tk()
root.config(bg="red")
root.geometry("400x400")
root.minsize(400,400)
root.maxsize(500,500)
# l1 = tkinter.Label(text="Welcome to python",font="Arial 22 bold")
f = tkf.Font(weight="bold")
l1 = tkinter.Label(text="Welcome \nto \npython",font=f,width=20,height=4)
# l1.config(font=("times new roman", "30" ,"bold"))
l1.config(borderwidth=2,anchor="se",relief="solid")
l1.pack()
root.mainloop()