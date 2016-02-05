# 'NDIGITS' RECURSION  (10 points possible)
# Write a function called ndigits, that takes an integer x (either positive or negative) as an argument. 
# This function should return the number of digits in x.

def ndigits(x):
    '''
    x: integer either positive or negative
    
    return: number of digits in x.
    '''
    if abs(x) / 10 < 1:
        return 1
    return ndigits(abs(x) / 10) + 1
        
        
    