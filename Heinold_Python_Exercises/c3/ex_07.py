"""Write a program that asks the user to enter an angle between 180 and 180. Using an
 expression with the modulo operator, convert the angle to its equivalent between 0 and
 360."""

angle = int(input("Enter an angle between -180 to 180 degrees: "))

equiv = angle % 360

print(f"The equivalent angle of {angle} is {equiv}")