 # there is three type of the method
 # 1 instance method 
 # 2 class method
 # 3 static method 
class student:
    school = "Shubham"

    def __init__(self,m1,m2,m3,m4):
         self.m1 = m1
         self.m2 = m2
         self.m3 = m3
         self.m4 = m4
    
    def avg(self):
        return (self.m1+self.m2+self.m3+self.m4)/4

    def get_m1(self):       # getter get the value don't need to use keyword get
        return self.m1

    #def set_m1(self,value): # setter set the value don't need to use keyword set
    #    return self.m1=value

    def getinfo(cls):
        return cls.school

s1 = student(30,20,44,25)
s2 = student(33,25,41,23)

print(s1.avg())
print(s2.avg())
print(school.getinfo())