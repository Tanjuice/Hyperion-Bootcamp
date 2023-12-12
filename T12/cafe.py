# A python program to calculate the total value of stock in an imaginary 
# cafe using lists and dictionaries

# Declare list for our menu
menu = ["Espresso", "Macchiato", "Cappuccino", "Americano"]


# Declare stock quantities
stock = {"Espresso": 100, "Macchiato": 50, "Cappuccino": 75, "Americano": 125}
# Declare product prices
price = {"Espresso": 1, "Macchiato": 2, "Cappuccino": 3, "Americano": 1.5}
# Create a new list to store totals
total = []

print(f"\t\t\t----- Stocktaker -----\n\nItem:\t\tTotal Value:\t Quantity:\t Item Price:\n")

# For loop taking the string names from menu and using it as a key to
# reference products in our stock and price dictionaries
for item in menu:
# Multiplies the corrisponding quantities by the prices for each product
# then adds to new variable "item_price"
    item_price = (stock[item] * price[item])
# Adds each value to "total" list
    total.append(item_price)
# Prints a summary of the product including:
# Item, total value of stock on site, stock qty & price per unit as reference
    print(f"{item}:\t£{item_price}\t\t {stock[item]}\t\t £{price[item]}\n")

# Sums up total 
total=(sum(total))

# Prints final total value of stock on site
print(f"-----------------\nTotal Stock Value On Site: £{total}\n-----------------")