# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.


print("Welcome to the error program")  # Syntax error: Missing brackets and unneccesary whitespace
print("\n")  # Syntax Removed whitespace and added brackets

# Variables declaring the user's age, casting the str to an int, and printing the result
age_str = "24"  # Syntax: Indented, == used instead of =. # Runtime: Cannot convert 'years old' to int 
age = int(age_str)  # also changed variable name to snakecase 
print(f"I'm {age} years old.") # Runtime - Not formatted with fstring and {} braces, too many comas

# Variables declaring additional years and printing the total years of age
years_from_now = 3.5  # Indentation error, declared as string.# Logical: changed to 3.5 to add the 6 months
total_years = age + years_from_now

print(f"The total number of years: {total_years}") # Missing brackets/fstring, incorrect variable name

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 # Syntax: Incorrect name, changed to total_years 
print("In 3 years and 6 months, I'll be ", total_months, "months old")  #Syntax: cannot concatenare int

#HINT, 330 months is the correct answer