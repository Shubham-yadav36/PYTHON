def rlist(list1):
    for name in list1 :
        return [name[::-1].title() for name in names]


names = ["shubham","ram","vijay"]
print(rlist(names))