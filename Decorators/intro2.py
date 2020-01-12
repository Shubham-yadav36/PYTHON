from functools import wraps
import time

t1 = time.time()
def outer_func(func):
    @wraps(func)
    def inside(*args,**kwargs):
        '''this is wraper function'''
        print("this is function decorator")
        return func(*args,**kwargs)
    return inside


t2 = time.time()

print(t2-t1)
@outer_func
def func1(n):
    print(f"this is function 1 : {n}")


@outer_func
def add(a,b):
    '''this is function add two number'''
    return "Sum is : " +str(a+b)


print(add(4,5))
print(add.__doc__)
func1('Shubham')
