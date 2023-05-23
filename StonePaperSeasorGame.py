# A Sample Game For Rock,Paper,Seasor
import random
from termcolor import colored

# Welcome to Our Game

print("Your Choice : ", ("Rock", 'Paper', 'Scissors'), sep='\n')
choice = ['Rock', 'Paper', 'Scissors']
x = random.choice(choice)

custom = input()
custom = custom.capitalize()
print(("You : ", custom))
print(("Computer : ", x))
if custom == x:
    print("Match Draw")
elif custom == 'Rock' and x == 'Scissors':
    print("You Win The Match Vigorously")
elif custom == 'Rock' and x == 'Paper':
    print("Sorry You Have Loose The Game....")
elif custom == 'Paper' and x == 'Rock':
    print("Unbelievable , You Beat The Computer")
elif custom == 'Paper' and x == 'Scissors':
    print("Sorry You Have Loose The Game....")
elif custom == 'Seasor' and x == 'Paper':
    print("What A Surprise , You Won That")
elif custom == 'Scissors' and x == 'Rock':
    print("It's A Sad Thing ....You Have Loose The Game....")
else:
    print(colored("Wrong Input ..... ", 'red'))
    print("Please Check Your Input Data Matches With The Following One Or Not", ("Rock", 'Paper', 'Seasor'))
