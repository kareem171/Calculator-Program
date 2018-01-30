#Area of a Rectangle


while True:
    print("This program calculates the area of a rectangle.")
    length = float(input("Enter length of rectangle:"))
    width = float(input("Enter width of rectangle:"))
    Area = length * width
    print("The area of the rectangle is", Area)
    user_input = input("Would you like to perform a new calculation? Y/N")
    if user_input== "Y" or user_input== "y":
        continue
    else:
        break
