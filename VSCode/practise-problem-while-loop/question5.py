n = int(input())
a = True
i = 0
while a:
    i += 1
    print (n,'x',i,'=',(n*i))
    if i == 10:
        a = False