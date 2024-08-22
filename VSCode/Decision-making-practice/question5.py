s_1 = eval(input("")) #side 1 of triangle
s_2 = eval(input("")) #side 2 of triangle
s_3 = eval(input("")) #side 3 of triangle

if s_1 == s_2 and s_2 == s_3:
  print ("equilateral triangle")
elif s_1 == s_2 or s_1 == s_3:
  print ("isosceles triangle")
else:
  print ("scalene triangle")