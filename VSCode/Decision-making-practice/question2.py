user = eval(input(""))
pwsd = eval(input(""))

if user == "admin":
  if pwsd == "password":
    print ("Welcome admin !!")
  elif pwsd == 12345:
    print ("Welcome, admin !! (warning: weak password)")
  else:
    print ("Incorrect password")
elif user == "guest":
  if pwsd == "guest":
    print ("welcome, guest !!")
  else:
    print ("Incorrect password")
else:
  print ("Unknown user. Please try again")