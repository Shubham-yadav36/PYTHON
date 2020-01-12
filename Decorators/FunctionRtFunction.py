def outFunc(msg):
    def innFunc():
        print(f"this is pass in outFunc : {msg}")
    return innFunc


fun1 = outFunc("Shubham")

def cal(n):
    def xPower():
        x = int(input("Enter term of power : "))
        return n**x
    return xPower


n = int(input("Enter number to calculated : "))
sq = cal(n)
print(sq())

