# greatest common divisor
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    ## --------------------------v1
    # smallest = a
    # largest = b
    # if a > b:
    #     smallest = b
    #     largest = a
    
    # if largest % smallest == 0:
    #     return smallest
    
    # while smallest > 1:
    #     if a % smallest == 0 and b % smallest == 0:
    #         ans = smallest
    #         break
    #     smallest -= 1
    # else:
    #     ans = 1
        
    # return ans
    
    ## ----------------------v2
    testValue = min(a, b)
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1
        
    return testValue
        
gcdIter(2, 12) # return 2
# gcdIter(6, 12) # return 6
# gcdIter(9, 12) # return 3
# gcdIter(17, 12) # return 1

# ------------------------------------------------------------structure of the problem
# The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

# Write an iterative function, gcdIter(a, b), that implements this idea. One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either reach a case where the test divides both a and b without remainder, or you reach 1.