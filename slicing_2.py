# Question:
# Given a list, reverse every k elements in place.
# Example Input:
arr = [1, 2, 3, 4, 5, 6, 7, 8]

# k = 3

# Expected Output:

# [3, 2, 1, 6, 5, 4, 8, 7]

#Hint: Use slicing with steps ([::-1]) inside a loop

for i in arr:
    y = i[::-1]
    print(y)

