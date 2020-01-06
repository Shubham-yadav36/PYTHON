l1 = [3,4,5,6,7]
l2 = [6,9,8,7,4]
l = list(zip(l1,l2))
l3,l4 = list(zip(*l))
print(l3)
print(l4)

new_list1 = [max(pair) for pair in zip(l1,l2)]
print(new_list1)