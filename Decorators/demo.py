def square(n):
    return n ** 2


def map_my(function, lis):
    return [function(i) for i in lis]


numbers = [10,2,4,4,5,6,9]
print(map_my(square,numbers))
