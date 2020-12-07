from tkinter import *
from tkinter import filedialog, messagebox


def accept():
    # file = filedialog.askopenfilename(initialdir="d:/Audio song/New song", title="select a song",
    #                                   filetypes=[("mp3 file", "*.mp3")])
    files = filedialog.askopenfilenames(initialdir="d:/Audio song/New song", title="select a song",
                                      filetypes=[("mp3 file", "*.mp3")])
    if files!="":
        messagebox.showinfo("Selected Song",files)
    else:
        messagebox.showinfo("Message", "You Did't select song")



root = Tk()
root.geometry("200x200")
btn = Button(root, text="Select Song", command=accept)
btn.pack()
root.mainloop()
