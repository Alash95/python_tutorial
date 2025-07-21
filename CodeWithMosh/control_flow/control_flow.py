"""comparison operators"""
10 > 3
10 >= 3
10 < 20
10 <= 20
10 == 10
10 == "10"
10 != "10"

print("bag" > "apple")
print("bag" == "BAG")
print(ord("b"))
print(ord("B"))

"""Conditional statements"""
temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")


"""Ternary operators"""
age = 22
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not eligible"

message = "Eligible" if age >= 18 else "Not eligible"
print(message)


"""logical operators
in python logical operators are short circuit

"""
high_income = False
good_credit = True
student = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")

if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")


if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")


"""chaining comparison operators"""
age = 18
if 18 <= age < 65:
    print("Eligible")


"""for loops"""
print("Sending a message")
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 4):
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 10, 2):
    print("Attempt", number + 1, (number + 1) * ".")

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

"""nested loops"""
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


print(type(5))
print(type(range(5)))
for x in "Python":
    print(x)
for x in [1, 2, 3, 4]:
    print(x)

number = 100
while number > 0:
    print(number)
    number //= 2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break
count = 0
for x in range(1, 10):
    number = x % 2
    if number == 0:
        count += 1
        print(x)
print(f"We have {count} even numbers")