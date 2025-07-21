"""Write a program that asks the user to enter two numbers, x and y, and computes x y
 x+y ."""

x = int(input("Enter a first number: "))
y = int(input("Enter a second number: "))

numerator = abs(x-y)
denominator = x + y

print(f"The answer is: {numerator / denominator}")
    