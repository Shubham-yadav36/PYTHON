import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Seditor")

# create label
name_lavel = ttk.Label(root, text="Enter Your Name : ").grid(row=0, column=0, sticky=tk.W)
age_level = ttk.Label(root,text="Enter Your Age : ").grid(row=1, column=0, sticky=tk.W)
email_level = ttk.Label(root,text="Enter Your Email: ").grid(row=2, column=0, sticky=tk.W)

#create entrybox
name_var = tk.StringVar()
name_entrybox = ttk.Entry(root, width=30, textvariable = name_var).grid(row=0,column=1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(root, width=30, textvariable = age_var).grid(row=1,column=1)

email_var = tk.StringVar()
email_entrybox = ttk.Entry(root, width=30, textvariable = email_var).grid(row=2,column=1)

#button
submit_button = tk.Button(root, text="Submit").grid( row=3, column=0)
root.mainloop()
