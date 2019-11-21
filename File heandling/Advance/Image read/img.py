f=open("sr.jpg",'rb')
f1=open("sr1.jpg",'wb')
for data in f:
    f1.write(data)