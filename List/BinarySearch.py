# in a binary search the list must be in sorted order
pos=-1
def find(list,n):
    l=0
    u=len(list)-1
    while l<= u:
        mid = (l+u)//2 # this the sign for integer division

        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1

    return False

list = [5,6,7,8,9,10,11,12]
n=1
if find(list,n):
    print("Found here",pos+1)
else:
    print("Not found")
