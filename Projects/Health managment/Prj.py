# Health Management System
def getdate():
    import datetime
    return datetime.datetime.now()
import datetime
def gettime():
    return datetime.datetime.now()

def take(k):
    if k == 1:
        c = int(input("enter 1 for Tips and 2 for Diating : "))
        if (c == 1):
            value = input("type here : \n")
            with open("Shubham-Tips.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Shubham-Diating.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 2):
        c = int(input("enter 1 for Tips and 2 for Diating :"))
        if (c == 1):
            value = input("type here\n")
            with open("Avinash-Tips.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Avinash-Tips.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 3):
        c = int(input("enter 1 for Tips and 2 for Diating : "))
        if (c == 1):
            value = input("type here\n")
            with open("Renuka-Tips.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Renuka-Diating.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(Shubham),2(Avinash),3(Renuka) : ")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for Tips and 2 for Diating : "))
        if (c == 1):
            with open("Shubham-Tips.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Shubham-Diating.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 2):
        c = int(input("enter 1 for Tips and 2 for Diating : "))
        if (c == 1):
            with open("Avinash-Tips.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Avinash-Diating.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 3):
        c = int(input("enter 1 for Tips and 2 for Diating"))
        if (c == 1):
            with open("Renuka-Tips.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Renuka-Diating.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (Shubham,Abinash,Renuka)")


print("Heath Management System : ")
a = int(input("Press 1 for submit the value and 2 for retrieve : "))

if a == 1:
    b = int(input("Press 1 for Shubham 2 for Abhinash 3 for Renuka : "))
    take(b)
else:
    b = int(input("Press 1 for Shubham 2 for Abhinash 3 for Renuka : "))
    retrieve(b)