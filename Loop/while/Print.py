name = input("enter your name : ")
carry = ""
i = 0
while i < len(name):
    if name[i] == carry :
        print(f" {name[i]}  :  {name.count(i)}")
        carry = name[i]
        i += 1