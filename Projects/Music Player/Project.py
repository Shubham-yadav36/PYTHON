import tkinter

root = tkinter.Tk()
root.title("Music Player")
img = tkinter.PhotoImage(file="audio.png")
root.iconphoto(root, img)

width = 1366 // 2
height = 763 // 2
x = 1366 // 4
y = 763 // 4
root.geometry(f"{width}x{height}+{x}+{y}")
root.resizable(False, False)
root.mainloop()
