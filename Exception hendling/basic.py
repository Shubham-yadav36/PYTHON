a = int(input("enter the 1st number:"))
b = int(input("enter the 2nd number :"))
try:
    print("open resourse")
    c = a / b;
    print(c)
except ValueError as e:
    print("Error : ", e)
except ZeroDivisionError as e:
    print("You can't divided by Zero : ", e)
except Exception as e:
    print("Error : ", e)
finally:
    print("Closed Resourse")
