
def transpose(l):
    print("The transpose is")
    for i in range(len(l[0])):
        print()
        for j in range(len(l)):
            print(l[j][i],end=" ")



l=[[1,2,3],[4,5,6],[7,8,9]]
print()
print("The matrix is")
for i in range(len(l)):
    print()
    for j in range(len(l[0])):
        print(l[i][j],end=" ")
print()
transpose(l)        
        
