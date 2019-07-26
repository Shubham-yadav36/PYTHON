class Ram:
    def info(self):
        print("this is the ram")

    def __init__(self):
        print("u are in Init in A")

class Raj(Ram):
    def __init__(self):
        super().__init__()
        print("u are in Init In B")

    def job(self):
        print("This is the Raj")

r = Raj()

print(r.info)