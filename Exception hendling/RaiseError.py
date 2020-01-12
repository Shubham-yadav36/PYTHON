def add(a,b):
    if (type(a) is int) and (type(b) is int):
        return a+b
    raise TypeError("you passed wrong data type value")


print(add("ram",5))