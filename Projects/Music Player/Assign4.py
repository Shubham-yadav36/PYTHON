import datetime
import tkinter

root = tkinter.Tk()
root.geometry('200x200+100+100')


def showdate():
    obj = datetime.datetime.now()
    l1 = tkinter.Label(text=obj.strftime("%d-%B-%Y, %H:%M:%S %p"))
    l1.pack()


b1 = tkinter.Button(root, text="Click Me", command=showdate)
b1.pack()
root.mainloop()
