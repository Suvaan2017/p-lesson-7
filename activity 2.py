units = int(input("Enter the number of units you consumed: "))
if(units < 50):
  amount = units * 2.60
  surcharge = 25
elif(units <= 100):
  amount = units * 2.90
  surcharge = 50
elif(units <= 200):
  amount = units * 3.20
  surcharge = 75
else:   
  amount = 130 + 162.50 + (units - 200) * 3.50
  surcharge = 100
total = amount + surcharge
print("The total amount to be paid is: ", total)
