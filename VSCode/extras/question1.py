m = int(input())
p = int(input())
c = int(input())
e = int(input())
a = int(input())
t = m+p+c+e+a
a,b = False,False
m_,p_,c_,e_,a_ = False,False,False,False,False
t_ = (t/125)*100
print ("The percentage is",t_)
if t >= 62.5:
    a = True
else:
    pass
if m>=20 and p >= 17.5 and c >= 17.5 and e >= 2.5 and a >= 5:
    b = True
else:
    pass

if a and b:
    print ('PASS in all Subjects')
    print ('PASS')
else:
    pass

if m<20:
    m_ = True
if p<17.5:
    p_ = True
if c<17.5:
    c_ = True
if e<2.5:
    e_ = True
if a < 5:
    a_ = True
else:
    pass

if m_:
    print ("FAIL in Math")
if p_:
    print ("FAIL in Physics")
if c_:
    print ("FAIL in Chemistry")
if e_:
    print ("FAIL in English")
if a_:
    print ("FAIL in Aptitude")

if t < 62.5 or m_ or p_ or e_ or c_ or a_:
    print ('FAIL')
else:
    pass
