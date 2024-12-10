# Here we are making a Quiz game
# it will ask bunch of question and if answered correctly thn
#it will enter 1 point to for the user
# and at the end of it  , it gives out the total points and
# percentage of it , eg . if 6 answered correctly out of 10 then
# "60 % answers are correct . "

print("Welcome to the Quiz")

#playing = input("Do you want to play ?  ")

# if playing != "yes" or "Yes" or "YES":
# this is wrong way of writing the 'or' condition
# either you can write with the condition fully , each comparison should be explicitly defined.or
#if playing != 'yes' and playing != 'Yes' and playing != 'YES':
# here we want to check all the three conditions to we need to use 'and' instead of 'or'
# make a list of the three 'yes' and then use the in keyword
# if the value entered is in the list
#if playing not in ['yes','YES','Yes']



# if playing != "yes" and playing != "Yes" and playing != "YES":
#     quit()

print("okay let's play")

point = 0

answer = float(input("How much do you get paid "))
if answer in (5.5,5,4.5) :
#if answer != "Capgemini" and answer != "CAPGEMINI" and answer != "Capgemini":
    print("correct !")
    point += 1
    print(point)
else:
    print("Incorrect")

#incase of avoiding lower case and upper case scenarios we
# use the .lower() function upon the input the user gives


answer = input("When will you be done with the course ? ")
if answer in ("March","January","February") :
#if answer != "Capgemini" and answer != "CAPGEMINI" and answer != "Capgemini":
    print("correct !")
    point += 1
    print(point)
else:
    print("Incorrect")

answer = input("How to much you plan to get in future ? ")
if answer in ("10Lpa","12Lpa","8Lpa") :
#if answer != "Capgemini" and answer != "CAPGEMINI" and answer != "Capgemini":
    print("correct !")
    point += 1
    print(point)
else:
    print("Incorrect")

answer = input("Who is your manager right now ? ")
if answer.lower() == "payal": #in ("John","Dan","Payal") :
#if answer != "Capgemini" and answer != "CAPGEMINI" and answer != "Capgemini":
    print("correct !")
    point += 1
    print(point)
else:
    print("Incorrect")

print(f"Congratulations you have scored {(point/4)*100}% in the quiz")







