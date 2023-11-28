# Program demonstrating how to modify text with different methods

# Raw input
string = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Replaces all '!' symbols with whitespace and prints
string = (string.replace("!", " "))
print(string)
# Prints string in uppercase using .upper
print(string.upper())
# Prints string backwards
print(string[::-1])