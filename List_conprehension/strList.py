list1 = [2.5,22,25.36,17,"shubham","nandini"]
list11 = [ str(i) for i in list1 if (type(i)==int or type(i)==float or type(i)==str)]
print(list11)