#Ask: roll the dice?
#if user enters y
#   Generate two random numbers
#   Print them
#If user enters n
#   Print thank you message
#   Terminate
#Else
#   print invalid choice    

from random import randint

count = 0
dice_roll = int(input(f"How many times do you want to roll the dice 🔢? "))
while True:
    prompt = input(f"Roll the dice? (y/n) 🎲: ").lower()

    if prompt == "y":
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        
        print(f"({dice1}, {dice2})")
        count += 1
        print(f"This is count {count} of {dice_roll}")

        if count == dice_roll:
            print("Thanks for playing!🤗")
            break

    elif prompt == "n":
        print("Thanks for playing!🤗")
        break

    else:
        print("Invalid choice!😡")



