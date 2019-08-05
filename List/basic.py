pos=0
def find(list,n):
    i=0

    while i< len(list):
        if list[i] == n:
            globals()['pos']=i
            return True
        i = i+1
    return False


list = [5,2,8,4,9,8]
n=9

if find(list,n):
    print("Found here",pos+1)
else:
    print("Not found")

