def iseven(n):
    return n%2==0


num = [2,3,4,5,56,67,6,98]
print(tuple(filter(iseven,num)))