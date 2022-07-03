print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
  print("Great you can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age <12:
    print("You have to pay $4.00")
  elif age <= 18:
    print("please pay $7.00")
  elif age >=50:
    print("Please pay $60.00")
  else:
    print("Please pay $12.00")      
else:
  print("Sorry, you have to grow taller before you can ride.")