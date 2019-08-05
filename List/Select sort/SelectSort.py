from typing import List


def sort(list):
    print("This is the of iteration under the selection sort : ")
    for i in range(len(list)-1):
        min = i
        for j in range(i,len(list)):
            if list[j]< list[min]:
                min = j

        t = list[i]
        list[i] = list[min]
        list[min] = t

        print(list)


num = [525,85,77,11,55,10,500,225]
sort(num)
print()
print("This is the sorted list",num)