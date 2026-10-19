# Travel Fare Calculator
FARE_RATE = 14

name = input("Enter passenger name: ")
while name.strip() == "":
    print("Name cannot be empty. Please enter a name.")
    name = input("Enter passenger name: ")

distance = input("Enter distance (km): ")
while not distance.isdigit() or int(distance) <= 0:
    print("Invalid input. Enter a number greater than 0.")
    distance = input("Enter distance (km): ")

distance = int(distance)

passengers = int(input("Enter number of passengers: "))
while passengers <= 0:
    print("Passengers must be a positive whole number.")
    passengers = int(input("Enter number of passengers: "))

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number
