# Python program to take a string and make each alternating character lower or uppercase
# Initialise starting string and output string as blank
string = "This is my custom string"
output_string = ""

# For loop for each letter in the length of the string 
for letter in range(len(string)):
# As iterations are numbered we can use them to alternate output
# Prints odd numbers as lower case and even as upper and add them to our blank list including whitespace
    if not letter % 2:
        output_string = output_string + string[letter].upper()
    else:
        output_string = output_string + string[letter].lower()

# Print final output
print(f"\n{output_string}")


# Starting with the same string it is split into a list by words and creates a new blank string
alternate_string = string.split()
new_string = ""
# Create counter to alternate over the list items
counter = 0

# For loops itterating over each item in the list and increases the counter and uses similar logic to before
for word in alternate_string:
    counter += 1
    if counter % 2:
# Updates blank string with each word and includes a space while alternating upper and lower
        new_string = new_string + (str(word).upper() + " ")
        
    else:
        new_string = new_string + (str(word).lower() + " ")

# Print final output
print(f"\n{new_string}")