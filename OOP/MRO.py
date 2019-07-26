# MRO --stands for mehthod resolution order tha 
# follow as left to right
class Ram:
    def info(self):
        print("this is the ram")

    def __init__(self):
        print("u are in Init in A")
    
    def In(self):
        print("this is the In A")

class Raj:
    def __init__(self):
        print("u are in Init In B")

    def job(self):
        print("This is the Raj")

    def In(self):
        print("this is the In B")

class Ramu(Ram,Raj):
    def __init__(self):
        super().__init__()
        super().In()
        print("u are in Init In C")

    def In(self):
        print("this is the In C")

r = Ramu()

print(r.In())