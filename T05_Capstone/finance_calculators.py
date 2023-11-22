# This is a python program consisting of 2 financial calculators
# 1 to calculate the return on investment using either simple or compound interest
# 1 to calculate the monthly repayment amount on a morgage based on value & interest 

import math

# Start Menu
print('''Finance Calculators:
Investment - to calculate the amount of interest you'll earn on your investment
Bond       - to calculate the amount you'll have to pay on a home loan''')
# User decides program
choice = input("\nEnter either 'Investment' or 'Bond' from the menu above to proceed:\n").lower()


# Investment Program
if choice == "investment":
# Inputs
  deposit = int(input("How much do you want to invest?\n"))
  rate = int(input("What is the interest rate? - Just add number\n"))
  rate2 = rate/100  # Make decimal for calc
  years = int(input("How many years are you investing for?\n"))
# Summary
  print(f"\n--Summary--\nTotal Deposit: £{deposit}\nInterest: {rate}%\nYears: {years}\n")

  interest = input("You you want the \'Simple\' or \'Compound\' interest?\n").lower()
# Simple interest Calc 
  if interest == "simple":
    total = deposit*(1 + rate2*years)
    print(f"\nThe total balance after {years} years is: £{total}\n")
# Compound interest Calc
  elif interest == "compound":
    total = deposit * math.pow((1+rate2),years)
    print(f"\nThe total balance after {years} years is: £{total}\n")


# Bond Program
elif choice == "bond":
# Inputs 
  value = int(input("What is the value of the property?\n"))
  rate = int(input("What is the yearly interest rate? - Just add number\n"))
  rate2 = rate/100  # Make decimal for calc
  m_rate = rate2/12 # Monthly rate of interest
  months = int(input("How many monthly payments?\n"))

# Monthly repayment Calc
  repayment = (m_rate * value)/(1- (1+m_rate)**(-months))

# Summary
  print(f"\n--Summary--\nProperty Value: £{value}\nMonths: {months}\nAt {rate}% interest\n")
# Result
  print(f"The monthly repayment is: £{repayment}\n")


# Error if neither option
else:
  print("Please enter a valid response")



