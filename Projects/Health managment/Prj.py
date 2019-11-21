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
            with open("Dharmendra-Tips.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Dharmendra-Tips.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 3):
        c = int(input("enter 1 for Tips and 2 for Diating : "))
        if (c == 1):
            value = input("type here\n")
            with open("Amit-Tips.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Amit-Diating.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(Shubham),2(Dharmendra),3(Amit) : ")


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
            with open("Dharmendra-Tips.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Dharmendra-Diating.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 3):
        c = int(input("enter 1 for Tips and 2 for Diating"))
        if (c == 1):
            with open("Amit-Tips.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Amit-Diating.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (Shubham,Dharmendra,Amit)")


print("Heath Management System : ")
a = int(input("Press 1 for submit the value and 2 for retrieve : "))

if a == 1:
    b = int(input("Press 1 for Shubham 2 for Dharmendra 3 for Amit : "))
    take(b)
else:
    b = int(input("Press 1 for Shubham 2 for Dharmendra 3 for Amit : "))
    retrieve(b)