num1 = int(input("enter first number : "))
num2 = int(input("enter first number : "))
num3 = int(input("enter first number : "))
print(isgreater(num1,num2,num3))

def isgreater(n1,n2,n3):
    if n1 > n2 and n2 > n3 :
        return n1
    elif n2>n3 and n2 > n1 :
        return n2
    else :
        return n3

def new_greter(n1,n2,n3) :
    big = isgreater(n1,n2)
    return isgreater(big,n3)
