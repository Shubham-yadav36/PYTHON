l1 = [3,4,5,6,7]
l2 = [6,9,8,7,4]
l3 = [8,4,3,2,4]
avg = []
def average(*args):
    for pair in zip(*args):
        avg.append(sum(pair)/len((pair)))
    return avg


print(average(l1,l2,l3))
average1 = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]


print(average1(l1,l2,l3))


new_l = [sum(pair)/len(pair) for pair in zip(l1,l2,l3)]
print(new_l)