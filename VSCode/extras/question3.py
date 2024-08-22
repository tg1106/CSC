n1 = int(input())
n2 = int(input())
c = 0
for i in range(n1,n2+1):
    if i%2==0:
        c += i
print (c)