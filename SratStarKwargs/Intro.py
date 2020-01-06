def prints(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")


prints(Name = "Shubham",age=25)
# dictionary unpacking
dict1 = {"Name" : "Shubham","Age" : 25}
prints(**dict1)