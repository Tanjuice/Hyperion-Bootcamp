''' Student register program asking how many students there are with their student ID numbers
and print to a new text file to be used as a register 
'''
print("\n--- Student Register ---\n")


# Get number of students to register & check it is a number
while True:
    # User Input
    student_qty = input("How many students would you like to enroll?: ")
    try: # Change value to integer
        student_qty = int(student_qty)
    except ValueError:
        print("Please enter a number\n")
        continue
    # If number can be converted, continue
    else:
        break

# Create an empty list
id_list = []

# For loop repeating for amount determined in input
for student in range(student_qty):
    
    # User Input
    id = input("Enter the student's ID #: ")
    
    # Add each ID to list
    id_list.append(id)

print("Writing Files......")

# Open/Create reg_form file and use id
with open ("reg_form.txt", "w") as output:
    # Create Header
    output.write("----- Student Register ----- \n\n")
    # For loop adding every ID to list with formatting
    for id in id_list:
        output.write("\n" + id + ": ....................\n")

print("Writing complete!")