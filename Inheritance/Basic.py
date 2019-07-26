class Shubham:
    def profesion(self):
        print("The work of the shubham is Software Devloper")

    def workplace(self):
        print("Shubham is work at google")

    def info(self):
        print("The shubham is never want to do govt. job whenever its't necessary")

class Renuka(Shubham): # Multi level inheritence
    def work(self):
        print("The renuka wnat a govt. job\n")

    def husband(self):
        print("Renuka want Husband who already have govt. job")

    def info(self):
        print("Renuka is the sensetive girl . she always cry")

class Married(Renuka):
    def Relation(self):
        print("Both Shubham and Renuka will be married")

R = Renuka()
S = Shubham()
M = Married()
print(M.workplace())
print(R.profesion())
print(R.info())