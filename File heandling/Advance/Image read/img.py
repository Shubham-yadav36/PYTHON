f=open("pic.jpg",'rb')
f1=open("renu.jpg",'wb')
for data in f:
    f1.write(data)