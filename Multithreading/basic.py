from threading import Thread
from time import sleep
class A(Thread):
    def run(self):
        for i in range(5):
            print("Hello!")
            sleep(1)

class B(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

a1 = A()
b1 = B()
a1.start()
b1.start()
