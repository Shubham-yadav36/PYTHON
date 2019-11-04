class Shubham:
    def profesion(self):
        print("The work of the shubham is Software Devloper")

    def workplace(self):
        print("Shubham is work at google")

    def info(self):
        print("The anyone is never want to do govt. job whenever its't necessary")

class Renuka: # Multiple inheritence
    def work(self):
        print("The anyone wnat a govt. job\n")

    def husband(self):
        print("anyone want Husband who already have govt. job")

    def info(self):
        print("anyone is the sensetive girl . she always cry")

class Married(hus,wife):
    def Relation(self):
        print("Both anyone and anyone will be married")

R = Renuka()
S = Shubham()
M = Married()
print(M.workplace())
print(R.profesion())
print(R.info())