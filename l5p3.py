# recursion by multiplication to solve exponent of
def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # base case, if exp <= 0
    if exp <= 0:
        # print("base case")
        return 1
    # if exp > 0 and exp is even
    elif exp % 2 == 0:
        # print("even")
        return recurPowerNew(base * base, exp/2) 
    # if exp > 0 and exp is odd
    else:
        # print("odd")
        return base * recurPowerNew(base, exp-1)
        
recurPowerNew(2, 3) # return 8

    