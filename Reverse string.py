# reverse a string
# Write a Python program to reverse a given string without using built-in functions.
from operator import truediv

s1 = ("cat")
# wrong approach
 s1 = list(s1)
# print(s1)
s2 = []
#
# for i in s1:
#     s2.append(i)
#     print(s2)



# Certainly! The range(start, stop, step) function in Python generates a sequence of numbers, and it is very flexible. Here's a breakdown of the components of range(len(s1)-1, -1, -1):
#
# start: len(s1)-1 — This is the index of the last character in the string s1.
# stop: -1 — This means the range will stop before index -1 (which corresponds to index 0 in Python, the first character).
# step: -1 — This tells Python to count backwards.
# More Examples with range(start, stop, step)

# We use len(s1)-1 to get the last valid index in the string s1.
# range(len(s1)-1, -1, -1) allows us to iterate through the string's indices in reverse order


for i in range(len(s1)-1, -1, -1):

    s2.append(s1[i])

# Join the list into a string again
reversed_string = ''.join(s2)
print(f"Reversed string: {reversed_string}")

# or
#
# reversed = s1[::-1]
# print(reversed)




