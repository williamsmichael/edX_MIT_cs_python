# ---------------------------version 1
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    if len(aTup) <= 1:
        return aTup
    return aTup[0::2]
    
# ---------------------------version 2

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # a placeholder to gather our response
    rTup = ()
    index = 0

    # Idea: Iterate over the elements in aTup, counting by 2
    #  (every other element) and adding that element to 
    #  the result
    while index < len(aTup):
        rTup += (aTup[index],)
        index += 2

    return rTup
    
print(oddTuples(())) # return ()
print(oddTuples((1,))) # return (1,
print(oddTuples((20, 4, 12, 16, 14, 4, 0)))



