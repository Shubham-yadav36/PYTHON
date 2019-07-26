class A:
    def show(self):
        print("In a class A")

class B(A):
    def show(self):
        print("In a class B")

s1=B()
s1.show()
