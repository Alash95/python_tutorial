"""Write a program that asks the user for their name and how many times to print it. The pro
gram should print out the user’s name the specified number of times."""

name = input('What is your name: ')
print_count = eval(input("How many times do i print your name: "))
for i in range(print_count):
    print(name)
