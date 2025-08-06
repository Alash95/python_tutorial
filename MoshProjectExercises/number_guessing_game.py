"""
Generate a random number
Loop
    Ask the user to make a guess
    if not a valid number
        print an error
    if number < guess
        print too low
    if number > guess
        print too high
    else
        print well done you guessed right
"""
from random import randint

best_score = None
while True:
    print("\n🎯 Welcome to the Number Guessing Game!")

    #Range and attempt from user input 
    min_num = int(input("What is the minimum number? "))
    max_num = int(input("What is the maximum number? "))
    attempts_allowed = int(input("How many attempts would you like? "))

    #generate number to guess
    number = randint(min_num, max_num)
    count = 0
    guesses = []

    while count < attempts_allowed:
        try:
            guess = int(input(f"Guess a number 🔢 (between {min_num} and {max_num}): "))
            count += 1
            guesses.append(guess)
            
            if  guess < number:
                print("Too low!🙏 Try again.")
                
            elif guess > number:
                print("Too high!🤭 Try again.")
            
            else:
                print(f"🎉Congratulations! You guessed the number in {count} out of {attempts_allowed} attempts")

                #Check and update the best score
                if best_score is None or count < best_score:
                    best_score = count
                    print(f"🏆 New best score is {best_score}")

                break

        except ValueError:    
            print("Invalid input! 😡, enter an integer 🔢")
    if guess != number:
        print(f"😭 You've used all {attempts_allowed} attempts. The number was {number}")
        print(f"Your guesses were: {guesses}")

    play_again = input("🔁 Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        print("Thanks for playing: 👋")
        if best_score:
            print(f"🥇 Your best score was {best_score} attempts")

        break
    
    





