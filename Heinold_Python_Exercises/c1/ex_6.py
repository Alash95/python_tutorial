"""Ask the user to enter a number ask_input. Use the sep optional argument to print out ask_input, 2ask_input, 3ask_input, 4ask_input,
 and 5ask_input, each separated by three dashes, like below."""

ask_input = eval(input("Input any number: "))
print(ask_input, ask_input * 2, ask_input * 3, ask_input * 4, ask_input * 5, sep="---")
