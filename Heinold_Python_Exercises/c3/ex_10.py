"""(a) One way to find out the last digit of a number is to mod the number by 10. Write a
 program that asks the user to enter a power. Then find the last digit of 2 raised to that
 power.
 """

# power = int(input("Enter a power in integer: "))
# mod = (2 ** power) % 10

# print(f"The last digit of {2 ** power} is {mod}")

"""(b) One way to find out the last two digits of a number is to mod the number by 100. Write
 a program that asks the user to enter a power. Then find the last two digits of 2 raised to
 that power.
"""

# power = int(input("Enter a power in integer: "))
# mod = (2 ** power) % 100

# print(f"The last digit of {2 ** power} is {mod}")

""" (c) Write a program that asks the user to enter a power and how many digits they want.
 Find the last that many digits of 2 raised to the power the user entered."""
power = int(input("Enter the power to raise 2 to: "))
num_digits = int(input("Enter how many last digits you want: "))

result = 2 ** power
mod_base = 10 ** num_digits

last_digits = result % mod_base
formatted_digits = str(last_digits).zfill(num_digits)

print(f"The last {num_digits} digits of {result} are: {formatted_digits}")