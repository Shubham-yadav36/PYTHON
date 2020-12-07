import tkinter
from tkinter import PhotoImage

root = tkinter.Tk()
root.minsize(400, 400)
strobj = tkinter.StringVar()
# img = tkinter.PhotoImage(file="D:/Wallpaper/Natural/Beach_1680x1050.jpg")
# l1 = tkinter.Label(root,borderwidth=2,relief="solid", text="Welcome", font="Arial 22 bold", bg="cyan", fg="black")

l1 = tkinter.Label(root,borderwidth=2,relief="solid", bg="cyan", fg="black",
                   textvariable=strobj)
l1.pack()

strobj.set("Text")

l1['bg'] = "blue"
l1['fg'] = "red"
print(l1.keys())
root.mainloop()



