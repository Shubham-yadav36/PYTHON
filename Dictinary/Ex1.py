def cube_dic(n):
    dic = {}
    for i in range(1,n+1):
        dic[i] = i**3
    return  dic

cube = cube_dic(10)
print(cube)