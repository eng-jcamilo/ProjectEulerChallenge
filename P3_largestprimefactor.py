""" Project 3: Largest prime factor """

def largestPrimeFactor(number):
    factors = []

    # First bucle is not considering if i is a prime factor.
    for i in range(2, number):
        while number % i == 0:
            number = number / i
            factors.append(i)
        
        if number == 1: 
            break

    return print("Largest prime factor found is %i." % max(factors))

if __name__ == '__main__':
    largestPrimeFactor(13195)
    largestPrimeFactor(600851475143)