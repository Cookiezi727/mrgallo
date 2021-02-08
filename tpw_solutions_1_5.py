# Exercise 1

print("Daniel Zhu")
print("17 Rainbow Roads")
print("Toronto, Ontario")
print("EFG 123")

# Exercise 2

userName = str(input("Please enter your name: "))
print(f"Hello there, {userName}!")

# Exercise 3

print("""# This program will calculate the area of a rectangle for you, in square meters, meaning all units should be in meters""")

width = float(input("Enter the width: "))
height = float(input("Enter the height: "))
area = width  * height

print(f"The area of the rectangle is {area} meters squared")

# Exercise 4

print("""# This program will take measurments in feet 
and calculate the area of a field, in acres. """)

width = float(input("Enter the width: "))
height = float(input("Enter the height: "))
areaInAcres = (width  * height) / 43560 # brackets are not necessary 

print(f"The area is {round(areaInAcres, 5)} acres" )

# Exercise 5

print("""This program will calculate your deposit based on the volume of your plastic containers.""")

smallerCont = int(input("Please enter the number of containers smaller or equal to 1L: "))
largerCont = int(input("Please enter the number of containers larger (but not equal) to 1L: "))
deposit = smallerCont * 0.1 + largerCont * 0.25
print(f"Your final deposit is ${round(deposit, 2)}.")
