win_num = 52
number = int(input("enter anu number 0 to 100:"))
guess = 1
over = False
while not over:
    if number == win_num:
        print(f"you win this game in {guess} time ")
        over = True
    else:
        if number > win_num:
            print("Number is too high")
            guess += 1
            number = int(input("Enter again : "))
        else:
            print("Number is too small")
            guess += 1
            number = int(input("Enter again :"))