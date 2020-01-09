""" Problem 1: Multiples of 3 and 5 """

def multiplesOf3and5(n):
    multiples = []

    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)

    return print("Sum of all multiples of 3 and 5 of %i is %i." % (n, sum(multiples)))

multiplesOf3and5(10)
multiplesOf3and5(1000)
