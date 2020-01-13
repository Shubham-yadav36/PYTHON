f=open("Shubham.txt",'r')
f1= open("Shubh",'a')
# print(f.readable())
# print(f.read())

for data in f:
    f1.write(data)


