"""Write a program that generates a random number, x, between 1 and 50, a random number y
 between 2 and 5, and computes xy."""

from random import randint

x = randint(1, 50)
y = randint(2, 5)

print(f"A random number between 1 and 50 is: {x}")
print(f"A random number between 2 and 5 is: {y}")
print(f"The exponent of {x} and {y} is: {x ** y}")