from functools import wraps

def only_allow(data):
    def makeup(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            if all([type(arg)==data for arg in args]):
                return func(*args,**kwargs)
            return "invalid data type passed"
        return wrapper
    return makeup


@only_allow(str)
def concat(*args):
    string = ""
    for arg in args:
        string += " " +arg
    return string


print(concat("ram","shyam","shubham"))