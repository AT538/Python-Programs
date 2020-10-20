import math
def circle():
    r=int(input("Enter radius"))
    a=math.pi*r*r
    print("Area is",a)


def square():
    s=int(input("Enter the side"))
    a=s*s
    print("Area is",a)


def rectangle():
    a=int(input("Enter length"))
    b=int(input("Enter breadth"))
    ar=a*b
    print("Area is",ar)


def triangle():
    b=int(input("Enter base"))
    h=int(input("Enter height"))
    a=(b*h)/2
    print("Area is",a)

circle();square();rectangle();triangle()    

    
    
