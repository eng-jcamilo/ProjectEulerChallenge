""" Project 2: Even Fibonacci numbers """

def fiboEvenSum(n):
    SEED_1 = 1
    SEED_2 = 2
    fibonacci = [SEED_1, SEED_2]

    # First step: Generate Fibonacci list.
    for i in range(2, n):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

    # Second step: Obtain even numbers inside Fibonacci list.
    even = [val for val in fibonacci if val % 2 == 0]

    return print("Even Fibonacci numbers sum of %i elements is %i." % (n, sum(even)))

fiboEvenSum(10)
fiboEvenSum(43)



