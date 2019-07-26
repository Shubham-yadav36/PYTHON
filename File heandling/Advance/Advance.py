"""This is the operation for write data"""
# f = open("file.txt","a")
# f.write("laptop")
# f.write("Mobile")
# f.write("this is the shubham yadav")
# f.write("this is the data of the shubham")


# copy the data of one file in another file
f = open("file.txt")
f1=open("File1.txt","w")
for i in f:
    print(i,end="")
    f1.write(i)


