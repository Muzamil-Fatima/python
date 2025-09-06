# Write a python program that calculate the radius of moon 
# Area = πr^2 => radius of moon 1,737.4 km
# with user input 
import math
radius = float(input("Enter the radius of the Moon: "))
area = 4*math.pi * radius * radius
print("Area of circle is :{0} ".format(area))
# without user input
import math
# Given surface area of the Moon (in square kilometers)
surface_area = 37932328.09938046  

# Calculate the radius
radius = math.sqrt(surface_area / (4 * math.pi))

print(f"Calculated radius of the Moon: {radius} km")
# -------------------------------------------------------------------------------------------------

# write a program  that calculate the no of doors of a car
def get_doors_by_type(car_type):
    """Return the number of doors based on car type."""
    car_type = car_type.lower()
    
    car_doors = {
        "sedan": 4,
        "suv": 4,
        "coupe": 2,
        "hatchback": 5,  # Rear hatch is counted as a door
        "convertible": 2,
        "truck": 2,  # Regular trucks usually have 2 doors
        "minivan": 5  # Includes sliding side doors
    }
    
    return car_doors.get(car_type, None)  # Return None if type not found

# Get user input
car_type = input("Enter the car type (Sedan, SUV, Coupe, Hatchback, etc.): ").strip()
doors = get_doors_by_type(car_type)

# If car type is unknown, ask for manual input
if doors is None:
    try:
        doors = int(input("Car type not recognized. Enter the number of doors manually: "))
    except ValueError:
        print("Invalid input! Defaulting to 4 doors.")
        doors = 4

print(f"The car has {doors} doors.")

