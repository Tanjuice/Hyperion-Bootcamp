# Python program to take a string and make each alternating character lower or uppercase
# Initialise starting string and output string as blank
string = "This is my custom string"
output_string = ""

# For loop for each letter in the length of the string 
for letter in range(len(string)):
# As iterations are numbered we can use them to alternate output
# Prints odd numbers as lower case and even as upper and add them to our blank string including whitespace
    if letter % 2:
        output_string += string[letter].upper()
    else:
        output_string += string[letter].lower()

# Print final output
print(f"\nAlternating Letters:\n{output_string}")


# Starting with the same string it is split into a list by words then create a new blank string and list
alternate_string = string.split()
final_list = []
final_string = ""

# Iterate over each item in the list and check if it is even or odd
# Cast word as upper or lower depending on thr above and append to final list
for word in range(len(alternate_string)):
    if word % 2:
        final_list.append(alternate_string[word].upper())
    else:
        final_list.append(alternate_string[word].lower())

# Join all words in the new list to create a new string seperated by a whitespace
final_string = " ".join(final_list)
# Print final result
print(f"\nAlternating Words\n{final_string}")