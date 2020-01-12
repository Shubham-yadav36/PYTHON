def func(n):
    for i in range(1,n+1):
        yield(i)


numbers  = func(10)
for i in numbers:
    print(i)
num = list(func(10))
print(num)