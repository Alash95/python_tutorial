"""Write a program that asks the user for a weight in kilograms and converts it to pounds. There
 are 2.2 pounds in a kilogram."""

ask_input = eval(input("Input your weight in ('Kg'/'Kilograms'): "))
unit_pound = 2.2
print(f"Your weight in pound is {ask_input * unit_pound}", end=".")