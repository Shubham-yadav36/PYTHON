from tkinter import *
from tkinter import simpledialog, messagebox


def accept():
    num = simpledialog.askinteger("Enter", "Enter Your Age ", minvalue=18, maxvalue=100)
    messagebox.showinfo("Voter Eligibility", "Your Are Valid Voter" + str(num))
    root.destroy()


root = Tk()
root.geometry("200x200")
btn = Button(root, text="Click Me", command=accept)
btn.pack()
root.mainloop()
