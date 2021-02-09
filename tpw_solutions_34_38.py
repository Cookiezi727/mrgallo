# Exercise 34

print("# This program will determine if an integer is even or odd. Integers only please.")
integer = int(input("Please enter an integer: "))

if integer % 2 == 0:
     print(f"{integer} is even!")
else:
    print(f"{integer} is odd")

# Exercise 35

print("# This program will covert human years to dog years.")
invalidInput = True

while invalidInput:
    humanYears = float(input("Please enter the number of years: "))
    if humanYears < 0:
        print("Please enter a postive number")
        invalidInput = True
    else:
        invalidInput = False

if humanYears < 2: 
        dogYears = humanYears * 10.5
        print(f"{humanYears} human years is {dogYears} in dog years!")
else:
    dogYears = (2 * 10.5) + (humanYears - 2) * 4
    print
    print(f"{humanYears} human years is {dogYears} in dog years!")

# Exercise 36

print("# This program will determine whether a letter is a vowel or a constanant, for those who don't know how to.")

letter = str(input("Please input ONE letter: ").lower())


if letter == "y":
    print("\"Y\" is sometimes a vowel, sometimes a constanant.")
elif letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("This letter is a vowel")
else:
    print("This letter is a constanant.")

# Exercise 37

print("This program will determine the name of the shape based on the number of sides, up to 10. Integer values only")

invalidInput = True
while invalidInput:
    numOfSides = int(input("Please enter the number of sides: "))
    if numOfSides <= 2 or numOfSides > 10:
        print("Invalid Input.")
        invalidInput = True
    else:
        invalidInput = False

if numOfSides == 3:
    name = "Triangle"
if numOfSides == 4:
    name = "Rectangle"
if numOfSides == 5:
    name = "Pentagon" 
if numOfSides == 6:
    name = "Hexagon"
if numOfSides == 7:
    name = "Septagon"
if numOfSides == 8:
    name = "Octagon"
if numOfSides == 9:
    name = "Nonagon"
if numOfSides == 10:
    name = "Decagon"

print(f"The name of a {numOfSides} sided shape is a {name}.")

# Exercise 38

print("This program will determine the number of days based on the month given")

validInput = False
while not validInput:
    month = str(input("Please enter a month: ").lower())
    if month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december":
        days = "31"
        validInput = True
    elif month == "april" or month == "june" or month == "september" or month == "november" :
        days = "30"
        validInput = True
    elif month == "febuary":
        days = "28 or 29"
        validInput = True
    else: 
        print("Please enter a valid month")
        validInput = False

print(f"This month has {days} days.")
