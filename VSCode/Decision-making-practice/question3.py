x = eval(input("Enter the coeffecient of x²: "))
y = eval(input("Enter the coeffecient of x: "))
z = eval(input("Enter the coeffecient of constant: "))

result = y**2 - 4*x*z
if result > 0:
  print ("The quadratic equation has 2 solutions")
elif result == 0:
  print ("The quadratic equation has exactly one solution")
else:
  print ("The quadratic equation has no solution")