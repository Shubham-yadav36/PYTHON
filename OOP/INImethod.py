class Shubh:

    def __init__(self, cpu, ram) :
        self.cpu=cpu
        self.ram=ram


    def prt(self):

        print(self.cpu, self.ram)


s1 = Shubh("AMD",15)
s2 = Shubh("INTEL",75)


s1.prt()
s2.prt()