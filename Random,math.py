'''
import random

print(random.random())
print(random.seed(5))

import random

options = ["Rock","Paper","Sissocr"]

user_choice = input("Choose:Rock,Paper,Sissors: ")

computer_choice = random.choice(options)

print(f"User choice is {user_choice}.Computer choice is {computer_choice}")

if user_choice == computer_choice:
    print("This is a TIe !")
elif user_choice == "Rock" and computer_choice == "Sissors":
    print("Rock Smashes Sissors Wins !")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("Paper Covers Rock Paper Wins !")
elif user_choice == "Paper" and computer_choice == "Sissors":
    print("Sissors cuts Paper YOU WIN ! !")
else:
    print("YOU LOSE !!")
'''
import random

Number = str(random.randint(5,10))
while True:
    user_input = input("Guess a Number between 5 to 10 to Win this Game!: ")
    if user_input == Number:
        print("YOU HAVE WON THE GAME !!")
        break
    else:
        print("Please try again")
    

    
