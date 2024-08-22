a = eval(input(""))
b = eval(input(""))
a = bool([(a**2)+(b**2) == (a+b)*(a-b)*(a*b)])
if a:
  print ("The path is symmetry")
else:
  print ("The path isn't symmetry")