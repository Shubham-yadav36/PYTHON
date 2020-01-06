def  sqlist1(ls) :
    list2 = []
    for i in ls:
            list2.append(i**2)
    return list2


num = list(range(1,11))
print(num)
print(sqlist1(num))


