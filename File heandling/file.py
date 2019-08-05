f=open("Shubham.txt",'r')
f1= open("renuka",'a')
# print(f.readable())
# print(f.read())

for data in f:
    f1.write(data)


