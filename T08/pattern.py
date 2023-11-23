# Python program that displays * symbols in an arrow or play shape
# Program to use an if-else statement but only 1 for loop


# Set inital number as a counter
number = 0


# If statement setting our loop quantity at 5
if number < 6:    
    # For loop printing "*" 1-5 times and adding 1 to the counter
    for num in range(1, 6):
        print("*" * num)
        number = number +1
                
else:
    pass

# While loop using the fact the counter is now at 5
while number > 0:
    number = number - 1 # Remove 1 from counter each itteration starting with "****"
    print("*" * number) # Continue printing "*" * the counter number until 0
    

