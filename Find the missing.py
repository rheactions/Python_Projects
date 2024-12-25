#You are given a list containing integers from 1 to n,
# with one number missing. Write a program to find the missing number.

list = [1,2,3,4,5,6,7,9,10]

for i in range(1,11):
    if i not in list:
        print(f"Missing number is {i}")

