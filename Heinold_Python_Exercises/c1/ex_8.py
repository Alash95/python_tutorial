"""Write a program that asks the user to enter three numbers (use three separate input state
ments). Create variables called total and average that hold the sum and average of the
 three numbers and print out the values of total and average."""

input1 = eval(input("Input a number 1: "))
input2 = eval(input("Input a number 2: "))
input3 = eval(input("Input a number 3: "))
total = input1 + input2 + input3
average = (input1 + input2 + input3) / 3
print(f"The total of {input1}, {input2}, {input3} is {total}\nThe average of {input1}, {input2}, {input3} is {average}")
