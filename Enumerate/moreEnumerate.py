def f_string(l,find):
    for pos,val in enumerate(l):
        if val== find:
            print(f"{pos} : {val}")
    return -1


names = ["shubham","ramesh","rajendra"]
f_string(names,"shubham")