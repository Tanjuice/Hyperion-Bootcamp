''' Program to calculate the cost of a holiday based on different perameters
sych as: location, hotel,flight & car rental costs based on number of days'''

# Set dicts for destinations and values
destinations = {
    "Milan": {"Flight": 250, "Hotel_cost": 150},
    "New York": {"Flight": 350, "Hotel_cost": 200},
    "London": {"Flight": 75, "Hotel_cost": 100}
}

# Displays destination options for while loop
def options():
    for key in destinations:
        print(key)

# Empty string to be used later after input from user
city_flight = ""
# Function to calculate hotel cost based on city and # nights
def hotel_cost(num_nights):
    if city_flight in destinations:
        hotel = destinations[city_flight]["Hotel_cost"] * num_nights
        return hotel

# Function to display flight cost based on city
def plane_cost(city):
    if city in destinations:
        flight = destinations[city]["Flight"]
        return flight

# Function to calculate car rentals
daily_cost = 50 # Fixed per day
def car_rental(rental_days):
    car = daily_cost * rental_days
    return car
    
# Calculate all of the prices together for a total cost
def holiday_cost(hotel, car, plane):
    holiday_cost = hotel + car + plane
    return holiday_cost


# Menu
print("\n----- City Break Calculator -----\n")
options()

''' While loop prompting user to choose an option and give a novel
response to the 3 options available while rejecting options 
not in our dictionaries '''
choice = "0"
while choice != "":
    choice = input("\nWhere would you like to go? (ctrl + c to exit)\n")
    if choice == "Milan":
        print("\nChe bello, goderti!\n")
        city_flight = choice
        break
    elif choice == "New York":
        print("\nIt's up to you...\n")
        city_flight = choice
        break
    elif choice == "London":
        print("\nEllo, ello, ello.\n")
        city_flight = choice
        break
    else:
        print(f"\nSorry, we dont have holidays in {choice} :-(\n")
        options()
        continue

# User input for # days
num_nights = int(input("How many days are you staying?\n"))
print(f"Ok, {num_nights} day(s) in {city_flight}. Sounds great!")

# User input for # of car rental days
rental_days = int(input("\nHow many days do you want to rent a car?\n"))
print(f"\n\nOk, {num_nights} day(s) in {city_flight} while renting a car for {rental_days} day(s). Sounds great!\n")

# Per night cost of hotel, used in summary section
day_rate = destinations[city_flight]["Hotel_cost"]
# Calculate per night cost by # nights
hotel = hotel_cost(num_nights)
print(f"Total cost for Hotel:\t£{hotel}\t\t--- £{day_rate} Per Night for {num_nights} nights(s)")

# Calculate per day cost of car rental
car = car_rental(rental_days)
print(f"Total Car Rental Cost:\t£{car}\t\t--- £{daily_cost} Per Day for {rental_days} day(s)")

# Calculate cost of plane ticket based on city
plane = plane_cost(city_flight)
print(f"Total Plane Cost:\t£{plane}")

# Combine the 3 values to get the total cost
total = holiday_cost(hotel, car, plane)
print(f"The total cost for this holiday is: £{total}")