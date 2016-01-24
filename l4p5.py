def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    # Your code here
    x = max(lo, x) # return lo when x is lower
    x = min(x, hi) # return hi when x is higher
    return x

print clip(5, 6, 7)
print clip(6, 5, 7)
print clip(5, 7, 6)