import math  

def main():
    first = int(input("First side: "))
    second = int(input("Second side: "))
    C = pythag(first,second)
    return C

def pythag(A,B):
    C = (A**2 + B**2)**0.5
    return C

print(main())
