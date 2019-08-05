def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                t = list[j]
                list[j] = list[j+1]
                list[j+1] = t


num = [6,8,9,10,2,5,14]
sort(num)
print(num)