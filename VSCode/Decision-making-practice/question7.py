inc = int(input())
if inc <= 100000:
  print ("No tax for you!")
elif inc >= 100001 and inc <= 300000:
  print ("tax =",inc*0.1)
elif inc >=300001 and inc <= 600000:
  print ("tax =", inc*0.2)
else: print ("tax =", inc*0.3)