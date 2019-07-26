class computer:
    def __init__(self):
        self.name="Renuka"
        self.age=21

    def update(self):
        self.name="Shubham"
    
    def compre(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = computer()
c2 = computer()
c2.age = 22
print("Before the updation :",c1.name)  # Before the updatioon
c1.update()     # if We update by the self this will impact on all progaram
print("Before the updation :",c1.name)  # after the updation
if c1.compre(c2):
    print("They are same")
else:
    print("They are not same")