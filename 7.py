l=[1,2,3,10,15]
n=int(input("Enter the item to be searched"))
def linear(l,n):
    f=0 
    for x in l:
        if x==n:
            print("Item found at position",l.index(x)+1)
            f=1
    if f==0:
            print("Item not present")



linear(l,n)            
            
