# Take input from user for the following values: Name, Age, House Number, Street Name.
# Print sentance containing all details of user

name = input("Hi! What is your name? ")
age = input(f"Hi {name}, how old are you? ")
house_num = input("OK, and what house number do you live at? ")
street = input("What street do you live on? ")

print(f"OK, so you are: \n{name} - {age} years old, and you live at: {house_num} {street}.")
