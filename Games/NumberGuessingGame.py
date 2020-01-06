import random
number = int(input("enter number : "))
wining_number = random.randint(1, 90)
win = False
terms = 1;
while not win :
    if number == wining_number :
        print(f"you win and your in {terms} times ")
        win = True
    else :
        if number < wining_number :
            print("too low ")
        else :
            print("too high")
        number = int(input("gas again"))
        terms += 1