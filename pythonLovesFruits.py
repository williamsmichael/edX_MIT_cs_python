# Code Grader: Python Loves Fruits (10 points possible)

def nfruits(fruitDict, pattern):
    '''
    fruitDict: A non-empty dictionary containing type of fruit and its quantity initially with Python when he leaves home (length < 10)
    pattern: A string pattern of the fruits eaten by Python on his journey as observed by Cobra.
    
    return : int maximum of the quantities of the three fruits.
    '''
    # go through the pattern except final index
    for letter in pattern[:-1]:
        
        # go through the fruitDict
        for key in fruitDict.keys():
            
            # decrease the relevant fruitDict key's value by one
            if letter is key:
                fruitDict[key] -= 1
            
            # increase the relevant fruitDict key's value by one 
            else:
                fruitDict[key] += 1
                
    # final index only decrease the relevant fruitDict key's value by one
    fruitDict[pattern[-1]] -= 1
        
    # return the highest value in the fruitDict 
    return max(fruitDict.values())

    
# test cases
# print nfruits({'E': 8, 'D': 5, 'F': 8, 'O': 7, 'R': 5, 'U': 10, 'W': 6, 'Y': 5}, 'Y') # return 10
# print nfruits({'A': 10, 'X': 5, 'N': 10, 'V': 10}, 'XVVX') # return 13
# print nfruits({'U': 8}, 'UUUUU') # return 3