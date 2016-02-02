# exponents multiplications by remainder
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # base case --> base = 1

    ## --------------------------------------v1
    # if exp == 0:
    #     result = 1
    #     return result
    # else:
    #     base *= recurPower(base, exp-1)
    #     return base
     
    ## --------------------------------------v2
    if exp <= 0:
        return 1
    return base * recurPower(base, exp - 1)
    
recurPower(2, 3) # return 8
# recurPower(2, 0) # return 1