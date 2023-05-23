# A Sample Game For Rock,Paper,Seasor
import random


choices = ["rock", "paper", "scissors"]
rules = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

user_score = 0
computer_score = 0


while True:

    user_choice = input("Enter your choice (rock, paper, scissors) or q to quit: ").lower()
    # Check if the user wants to quit
    if user_choice == "q":
        break
    # Check if the user's choice is valid
    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue
    # Get the computer's choice randomly
    computer_choice = random.choice(choices)
    # Print both choices
    print(f"You chose {user_choice}. Computer chose {computer_choice}.")
    # Compare the choices and update the scores
    if user_choice == computer_choice:
        print("It's a tie.")
    elif rules[user_choice] == computer_choice:
        print("You win!")
        user_score += 1
    else:
        print("You lose.")
        computer_score += 1
    # Print the current scores
    print(f"Your score: {user_score}. Computer score: {computer_score}.")


print("Game over.")
print(f"Your final score: {user_score}. Computer's final score: {computer_score}.")
