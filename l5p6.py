# Write an iterative function, lenIter, which computes the length of an input argument (a string), by counting up the number of characters in the string.
def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    count = 0
    for letter in aStr:
        count += 1
    return count
    
print(lenIter("create"))