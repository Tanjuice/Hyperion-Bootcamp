# # Python program to read data from a text file and output the data seperated by names/DOB's

# Create list for each item 
names = []
dob = []

# Opens DOB.txt from folder in read mode and create variable called file
with open('DOB.txt', 'r') as file:
    for line in file:
# Split each line into seperate list items
        line = line.split()
# Create name & date variables. Join into single strings the elements based on position in list
        name = " ".join(line[0:2])
        date = " ".join(line[2:5])
# Add newly formatted string to lists
        names.append(name)
        dob.append(date)        

# Use for loop to display results in format requested
print("\n --- Names --- \n")
for name in names:
    print(name)

print("\n --- DOB --- \n")
for date in dob:
    print(date)
