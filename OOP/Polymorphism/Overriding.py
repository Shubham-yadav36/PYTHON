class school:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        elif a!=None:
            s=a
        return s
s1=school(20,30)

print(s1.sum(20,10,50))
print(s1.sum(20,30))
print(s1.sum(10))