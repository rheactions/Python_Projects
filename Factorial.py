#Write a Python function to calculate the factorial of a number using recursion.
# The factorial of n is n * (n-1) * (n-2) * ... * 1.
#for instace
# 5! = 5 * 4 * 3 * 2 * 1


import  math

n = int(input("enter the number: "))

def factorial(n):

    if n == 0  | n == 1:
        return 1
    else:
        result = math.prod(range(2, n + 1))  # This is the same as 1*2*3*4*5

    print(result)

factorial(n)



# this would be wrong if ended here
#cuz 1! is 1 and 0! is also 1
