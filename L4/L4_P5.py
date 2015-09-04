import random
x = random.randint(1, 100)

def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    # Your code here
    # if x is lower than lo return lo otherwise x
    # if x is greater than hi return hi otherwise x

    print(x)

    # version 1
    # x = max(x, lo)
    # x = min(x, hi)
    # return x

    # version 2
    return min(max(x, lo), hi)

print(clip(10, x, 50))
