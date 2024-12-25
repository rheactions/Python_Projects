#take a list and find out the prime numbers

# primes - divisible by 1 and itself
# - should be grater than 1

n = int(input("enter n : "))
def primes(n):
    if n <= 1:
        return False
    elif n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3,n,2):
        if n % i == 0:
            return False
    return True

if primes(n)== True:
    print("prime")

else:
    print("not prime")

