#sum of even numbers
#Write a Python program to sum all even numbers from a list of integers.


# input and output
#define a list
#find the even numbers
#add them on

numbers = [2,1,4,5,6,7,8]
evens = []
total = 0
for i in numbers:
    if i % 2 == 0:
        evens.append(i)
        total = sum(evens)
print(total)




