from functools import wraps

def evedec(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        evelist = []
        if all([type(arg)==int for arg in args ]):
            return func(*args,**kwargs)
        return "invalid arguement"
        # for arg in args:
        #         evelist.append(type(arg)==int)
        # if all(evelist):
        #     return func(*args,**kwargs)
        # else:
        #     return "invalid arguement"
    return wrapper


@evedec
def take(*args):
    total=0
    for i in args:
        total += i
    return total


print(take(4,5,6,9,8,7,7,9))
    