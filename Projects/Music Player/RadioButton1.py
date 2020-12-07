from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser


def show():
    if col.get() == 'male':
        messagebox.showinfo("Gender", "Your select : Male ")
    else:
        messagebox.showinfo("Gender", "Your select : Female ")


root = Tk()
root.geometry('200x200')
col = StringVar()
lb = Label(text="Select Your Gender : ")
btn1 = Radiobutton(root, text='Male', variable=col, command=show, value="male")
btn2 = Radiobutton(root, text='Female', variable=col, command=show, value="female")
btn1.deselect()
btn2.deselect()
lb.pack()
btn1.pack()
btn2.pack()
root.mainloop()
