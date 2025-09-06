# Q1. Write a python program that calculate the radius of moon 
import math
# Given surface area of the Moon (in square kilometers)
surface_area = 37932328.09938046  

# Calculate the radius
radius = math.sqrt(surface_area / (4 * math.pi))

print(f"Calculated radius of the Moon: {radius} km")
# =====================================================================================================
# write a program  that calculate the no of doors of a car

# Ask the user for the car type
car_type = input("Enter the type of car (Sedan, SUV, Coupe, etc.): ").strip().lower()

# Define common car door numbers
door_count = {
    "sedan": 4,
    "suv": 4,
    "coupe": 2,
    "pickup": 2,  # Some pickups have 4 doors
    "minivan": 4
}
# Get the number of doors based on car type
num_doors = door_count.get(car_type, "Unknown (varies by model)")

print(f"The {car_type.capitalize()} typically has {num_doors} doors.")
# ===================================================================================================
# Q3. Write a program that execute  the tabel of 10 in reverse order?

# Program to print the table of 10 in reverse order using while loop
number = 10  # The number whose table we want
i = 10  # Start from 10
while i >= 1:
    print(f"{number} x {i} = {number * i}")
    i -= 1  # Decrement i
# =================================================================================================
# Q4. Write a program to check either given year is a leap year
# Program to check if a given year is a leap year

year = int(input("Enter a year: "))

# Check leap year conditions
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is NOT a Leap Year.")

# =================================================================================================
# Q5. write a program that calculate the LCM of two number.
import math

# Function to calculate LCM
def calculate_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)  # LCM formula
# Taking input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# Compute LCM
lcm = calculate_lcm(num1, num2)
print(f"LCM of {num1} and {num2} is: {lcm}")
# ================================================================