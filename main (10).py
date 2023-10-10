n = int(input("Enter a year: "))

if(n %400 == 0) and (n % 100 == 0):
  print("Leap year")
elif(n % 400 != 0) and (n % 100 !=0):
  print("Not a Leap year")