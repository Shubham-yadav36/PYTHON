def outer_func(func):
    def inside():
        print("this is function decorator")
        func()
    return inside


@outer_func
def func1():
    print("this is function 1")


func1() 
@outer_func
def func2():
    print("this is function 2")


func1()

# func1 = outer_func(func1)
# func1()
# func2 = outer_func(func2)
# func2()