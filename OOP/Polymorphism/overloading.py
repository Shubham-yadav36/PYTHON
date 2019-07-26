# in the python we cant have the concept of the method oveloading

class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)
        return s3

    def __mul__(self, other):
        c1 = self.m1*other.m1
        c2 = self.m2*other.m2
        c3 = student(c1,c2)
        return c3

    def __gt__(self, other):
        n1=self.m1+self.m2
        n2=other.m1+other.m2
        if n1>n2:
            return True
        else:
            return False

s1 = student(50,100)
s2 = student(20,140)
s3  = s1 + s2
c3 = s1*s2
print(c3.m1)
print(s3.m1)
print(s3.m2)

if s1>s2:
    print("s1 wins")
else:
    print("S2 wins")