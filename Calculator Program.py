#Calculator App

'''
Build a calculator app that provides the amount of miles per gallon

miles per gallon = milesDriven/gallonsUsed

'''
while True:
    print("This program calculates mpg.")
    miles_driven = float(input("Enter miles driven:"))
    gallons_used = float(input("Enter gallons used:"))
    mpg = miles_driven/gallons_used
    print("Your miles per gallon is", mpg)
    user_input = input("Would you like to perform a new calculation? Y/N")
    if user_input== "Y" or user_input== "y":
        continue
    else:
        break
