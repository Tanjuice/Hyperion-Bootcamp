# A python program that asks for inputs until the user enters '-1'
# Program will then calculate the average of the numbers entered not including '-1'

# Create list of future inputs
total_input = []
# Declare initial input converted to an integer
number = int(input("Please enter a number - Type '-1' to quit: "))

# While loop asking for input and check if '-1' is entered
while number > -1:
  # Add input to list
  total_input.append(number)
  # Summerize and ask for another input
  print(f"\nCurrent list: {total_input}")
  number = int(input("Please enter a number - Type '-1' to quit: "))

# Calculate the average of the inputs
average = sum(total_input)/len(total_input)

# Outputs
print(f"\nHere are all of your inputs: {total_input}")
print(f"The average number from your list is: {average}\n")

    




