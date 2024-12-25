#Write a function that removes duplicates
# from a list without using a set.
from zoneinfo import reset_tzpath

fruit = ['apple','mango','grape','apple']
uniques = []

for i in fruit:
    if i not in uniques:
        uniques.append(i)

print(uniques)



