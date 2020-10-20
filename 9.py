m=[[1,2],[3,4]]
n=[[5,6],[7,8]]
def add(m,n):
    print("Sum is")
    for i in range(len(m)):
        print()
        for j in range(len(m[0])):
            print(m[i][j]+n[i][j],end=" ")



def sub(m,n):
    print("\n Difference is")
    for i in range(len(m)):
        print()
        for j in range(len(m[0])):
            print(m[i][j]-n[i][j],end=" ")


def mul(m,n):
    print();print()
    print("Product is")
    result=[[0,0],[0,0]]
    for i in range(len(m)):
        for j in range(len(n[0])):
            for k in range(len(n)):
                result[i][j]+=m[i][k]*n[k][j]


    for i in range(len(result)):         
        print()
        for j in range(len(result[0])):
             print(result[i][j],end=" ")



add(m,n)
sub(m,n)
mul(m,n)
    
              
