class Car:
    wheel=4             # this is the class variable
    def __init__(self):
        self.mil=30     #that's called instance variable because they are in method/procedure
        self.mod="BMW"
s1 = Car()
s2 = Car()
s1.mod="Lambadghihini"
print(s1.wheel)
print(s1.mil,s1.mod)
print(s2.mil,s2.mod)