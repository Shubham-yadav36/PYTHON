def evefunc(n):
    for number in range(1,n+1):
        if number%2==0:
            yield(number) 


list1 = list(evefunc(10))
print(list1)