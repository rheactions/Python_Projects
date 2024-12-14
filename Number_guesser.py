import random

#so random is a default module , but you can also create
#your own modules and if you need to import any modules
#from someone else you need to install it first

top_of_range = input('Type a number:')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a Num larger than 0 , next time!")
        quit()

else:
    quit()
    print("Please type a digit")


random_number = random.randint(0,top_of_range)

#last number will not be included
#when you run it each time , there will be a random no in the output
# if the starting number is not mentioned then the it will from 0

#   Note if you incase wish to pick random items as in strings
#from list you can use the method random.choice(listname)

Guesses = 0
while True:
    user_g = input("Please make a guess:")
    Guesses += 1
    if user_g.isdigit():
        user_g = int(user_g)
    else:
        print("please enter a number.")

    if (user_g == random_number):
        print("You got it.")
        break
    elif user_g > random_number:
        print("You have guessed above the actual number")
    elif user_g < random_number:
        print("You have guess below the actual number")
    else:
        print("Try again !")

#random_number = random.randrange(top_of_range)

# we wanna use randint() instead cuz , it will include both start and stop values
print(random_number)
print("you guessed it in",Guesses,"tries")



