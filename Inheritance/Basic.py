class Shubham:
    def profesion(self):
        print("The work of the shubham is Software Devloper")

    def workplace(self):
        print("Shubham is work at google")

    def info(self):
        print("Private")
    
-
class Dharam(Shubham): # Multi level inheritence
    def work(self):
        print("The  wnat a govt. job\n")

    def husband(self):
        print("Married")

    def info(self):
        print("Fail")

class Married(Dharam):
    def Relation(self):
        print("Passed")

R = Dharam()
S = Shubham()
M = Married()
print(M.workplace())
print(R.profesion())
print(R.info())