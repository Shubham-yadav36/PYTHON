from tkinter import *
from tkinter import filedialog, messagebox


def accept():
    files = filedialog.askopenfilenames(initialdir="d:/Audio song/New song", title="select a song",
                                      filetypes=[("mp3 file", "*.mp3")])
    if type(files) is tuple:
        sname = ""
        for s in files:
            sname += s + "\n"
        lb1.config(text = sname)
    else:
        messagebox.showinfo("Message", "You Did't select song")



root = Tk()
root.geometry("200x200")
btn = Button(root, text="Select Song", command=accept)
lb1 = Label(root,text="Your Selected Files \n")
btn.pack()
lb1.pack()
root.mainloop()
