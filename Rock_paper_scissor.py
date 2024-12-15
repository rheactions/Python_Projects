#first we are going tii import the random module

import random

user_wins = 0
comp_wins = 0


options = ['rock','paper','scissors']


while True:
    user_input = input("Type Rock/Paper/Scissor or Q to Quit: ").lower()

    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)

    comp_pick = options[random_number]
#here we are using the random number feature to randomly pick
# a index number
    print("computer's choice is ", comp_pick)

    if user_input == 'rock' and comp_pick == "scissors":
        print("user wins")
        user_wins += 1


    elif user_input == "paper" and comp_pick == "rock":
        print("user wins")
        user_wins += 1

    elif user_input == "scissors" and comp_pick == "paper":
        print("user wins")
        user_wins += 1

    else:
        print("you lost")
        comp_wins += 1


print("You won ",user_wins,"times")
print("Comp won",comp_wins,"times")




