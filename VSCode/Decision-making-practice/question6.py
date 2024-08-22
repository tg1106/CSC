age = eval(input())
if age < 0:
  print ("Invalid age")
elif age >= 0 and age <= 12:
  print ("child")
elif age >= 13 and age <= 19:
  print ("Teenage")
elif age >=20 and age <= 59:
  print ("Adult")
else:
  print ("Senior")