# Problem 6
# (15 points possible)
# Write a function to flatten a list. The list contains other lists, strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5]

def flatten(aList):
    ''' 
    aList: a list 

    Returns a copy of aList, which is a flattened version of aList 
    '''
    
    # success!
    # for item in aList:
    # if type(item) is list:
    #     flatten(item)
    # else:
    #     print item
    
    final = []
    for item in aList:
        if type(item) is list:
            final.extend(flatten(item))
        else:
            final.append(item)
    return final

print flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]) 
# return [1,'a','cat',2,3,'dog',4,5]

# Recursion is extremely useful for this question. You will have to try to flatten every element of the original list. To check whether an element can be flattened, the element must be another object of type list.

# Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements. Note that we ask you to write a function only -- you cannot rely on any variables defined outside your function for your code to work correctly.