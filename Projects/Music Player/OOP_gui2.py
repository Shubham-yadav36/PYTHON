from tkinter import *


class MyFirstGui:
    def __init__(self, root):
        self.root = root
        self.root.title('My Gui')
        self.root.geometry('300x400')
        self.lb1 = Label(self.root, text="0", bg='cyan', fg='red')
        btn1 = Button(self.root, text='click me', command=self.count)
        btn2 = Button(self.root, text='Quit', command=lambda: self.root.destroy())
        self.lb1.pack()
        btn1.pack()
        btn2.pack()
        self.i = 0

    def count(self):
        self.i += 1
        self.lb1.config(text=f"{self.i}")


root = Tk()
mygui = MyFirstGui(root)
root.mainloop()
