def all_prints(*args):
    print(args)


def all_total(*args):
    total=0
    for i in args:
        total += i
    return total


all_prints(10,20,1,25,41,21)
print(all_total(10,20,1,25,41,21))


