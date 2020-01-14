""" Project 4: Largest palindrome product """

def largestPalindromeProduct(n):
    SEED = int('9' * n)
    palindromes = []

    # We should find largest palindrome product.
    # In that case we start from the top of the range.
    for i in range(SEED, 0, -1):
        for j in range(SEED, 0, -1):
            val = i * j
            # Reversing the product result.
            # Without casting str->int is not possible make a comparison.
            r_val = int(str(val)[::-1])

            if val == r_val:
                palindromes.append(val)
                break 

    return print("Largest palindrome of %i digits product is %i." % (n, max(palindromes)))

if __name__ == '__main__':  
    largestPalindromeProduct(2)
    largestPalindromeProduct(3)
    largestPalindromeProduct(4)