odd = []
even = []
list1 = [odd.append(i) if i%2==0 else even.append(i) for i in range(1,20)]
print(list1)