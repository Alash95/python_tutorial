"""Write a program that asks the user for an hour between 1 and 12 and for how many hours in
 the future they want to go. Print out what the hour will be that many hours into the future.
 Anexample is shown below."""

current_hour = int(input("Enter an hour between 1 and 12: "))
hours_ahead = int(input("How many hours in the future do you want to go? "))
new_hour = (current_hour + hours_ahead) % 12

if new_hour == 0:
    new_hour = 12
    print(f"New hour: {new_hour} o'clock")
else:
    print(f"New hour: {new_hour} o'clock")

