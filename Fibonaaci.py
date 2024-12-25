# 0,1,1,2,3,5,8,13,21,..

fib = [0,1]

def fibbo(n):
    for i in range(2, n):
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)
        # The issue with your code is that the
        # return fib statement is inside the loop,
        # which causes the function to return after
        # the first iteration of the loop.
        # As a result, the function exits after
        # computing just the first Fibonacci number after the initial two numbers (0 and 1), instead of completing the entire Fibonacci sequence up to n terms.
    return fib



print(fibbo(10))



