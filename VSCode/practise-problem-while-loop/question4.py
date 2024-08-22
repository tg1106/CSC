#Factorial of a number using while loop in Python
a,b = 0,1
n = int(input())
print (a,b,end=" ")
while n>0:
    c = a+b
    print (c,end = " ")
    a = b
    b = c
    n=n-1