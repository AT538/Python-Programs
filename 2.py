
def perfect(n):
    s=0
    i=1
    while i<n:
        
        if n%i==0:
            s+=i
        i+=1
    if s==n:
        print("The number is perfect")
    else:
        print("The number is not perfect")

n=int(input("Enter a number"))
perfect(n)        
