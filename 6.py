n=int(input("Enter the number of rows"))
def pascal(n):
    for i in range(n):
        print()
        x=1
        for k in range(i+1):
            print(x,end=" ")
            x=(x*(i-k))//(k+1)



pascal(n)            
