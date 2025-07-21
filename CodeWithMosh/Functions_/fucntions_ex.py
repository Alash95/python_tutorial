# def greet2():
#     print("Hi there")
#     print("Welcome aboard")


# greet2()


# def greet1(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")


# greet1("Mosh", "Hamedani")


# def greet(name):
#     print(f"Hi {name}")


# def get_greeting(name):
#     return f"Hi {name}"

# # message = get_greeting("Mosh")
# # file = open("content.txt", "w")
# # file.write(message)


# print(greet("Mosh"))

# """keyword argument/default args"""


# def increment(number, by=1):
#     return number + by


# print(increment(2))


"""xxargs"""
# def save_user(**user):
#     print(user["name"])

# save_user(id=1, name="John", age=22)

# message = "a"

# def greet(name):
#     global message
#     message = "b"

# greet("Mosh")
# print(message)
"""augmented assignemnt operators"""
"""xargs/ debugging F9,F10,F11, Shift + F11"""
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# print("Start")
# print(multiply(1, 2, 3))


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if ((input % 3) == 0):
        return "Fizz"
    if ((input % 5) == 0):
        return "Buzz"
    return input
    

print(fizz_buzz(7))




