""" Ask the user to enter a number. Print out the square of the number, but use the sep optional
 argument to print it out in a full sentence that ends in a period. Sample output is shown
 below."""

ask_input = eval(input("Enter a number: "))
print(f"The square of {ask_input} is {ask_input ** 2}", end=".")
