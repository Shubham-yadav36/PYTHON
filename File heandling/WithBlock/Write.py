# with open("file.txt","w") as f:
#     f.write("this is the file name as file.yxy") # data overite

# with open("file.txt","a") as f: # apped if not present create
#     f.write("this is the file for the writing.")

# r+ mode
#if we want to write from last
# with open("file.txt","r+") as f:
#     f.seek(len(f.read()))
#     f.write("i am the best programmer\n")
#     print(f.read())

with open("file.txt","r") as rf:
    with open("Shubh","w") as wr:
        wr.write(rf.read())