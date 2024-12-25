#Write a Python function that reverses a
# given list in place, meaning you cannot
# create a new list to store the result.
# Modify the original list directly.

list = list(input("enter the list:"))
def reverse (list):
    left = 0
    right = len(list) - 1

    while left < right:
        list[left],list[right] = list[right],list[left]

        left += 1
        right -= 1

    print(list)

reverse(list)