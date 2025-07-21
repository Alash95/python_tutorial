"""Write aprogramthataskstheuserforanumberofsecondsandprintsouthowmanyminutes
 and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. [Hint: Use the //
 operator to get minutes and the % operator to get seconds.]"""

num = int(input("What is the number of seconds: "))

minutes = num // 60
seconds = num % 60

print(f"{num} seconds is {minutes} minutes and {seconds} seconds")
