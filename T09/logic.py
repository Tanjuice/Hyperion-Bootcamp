# This is a python program that displays a logical error

# Take input from user
number = input("Please enter a number: ") # Input has not been cast to an integer

print(f"{number} * 5 =", number * 5) # String is multiplied instead of int
