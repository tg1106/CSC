n = int(input())
for i in range (n):
    print (' '*(n-1-i),end = '')
    for j in range (i):
        print ('*','',end = "")
    print ()
