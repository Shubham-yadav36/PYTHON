def arg_para(num , *args):
    if num :
        return [i**num for i in args]
    else:
        print("you didn\"t pass any arguemendt")


list1 =[14,55,11,24,21,2,1,2,11,44,]
print(arg_para(2,*list1))