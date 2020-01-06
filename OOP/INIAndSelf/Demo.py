class Shubham:
    def __init__(self):
        self.age=20

    def update(self):
        self.age=90

    def compare(self,other):
        if self.age == other.age:
            print("they are same ")
        else:
            print("they are not same")


c1 = Shubham()
c2 = Shubham()


c1.update()
c1.compare(c2)
