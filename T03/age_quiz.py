# Welcome message
print("Welcome to the age quiz!")

# Take input and change to an int
age = int(input("How old are you? "))

# Based on input display message. Max age is set to 100
if age > 100:
  print("Sorry you're dead.")
elif age >= 65:
  print("Enjoy your retirement!")
elif age >= 40:
  print("You're over the hill!")
elif age == 21:
  print("Congrats on your 21st!")
elif age < 13:
  print("You qualify for the kiddie discount.")
else:
  print("Age is but a number.")
