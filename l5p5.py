# greatest common divisor - Euclidean Algorithm

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
        
    if b <= 0:
        # base case
        return a
    return gcdRecur(b, a % b)
    
# test cases
gcdRecur(2, 12) # return 2
# gcdRecur(6, 12) # return 6
# gcdRecur(9, 12) # return 3
# gcdRecur(17, 12) # return 1

# description:
# The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,
# A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:
# If b = 0, then the answer is a
# Otherwise, gcd(a, b) is the same as gcd(b, a % b)
# Write a function gcdRecur(a, b) that implements this idea recursively. This function takes in two positive integers and returns one integer.