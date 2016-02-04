def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    ans = None
    biggest = 0
    for key, value in aDict.items():
        if len(value) >= biggest:
            biggest = len(value)
            ans = key
    print(ans)
    return ans
    
# print biggest({'a': ['aardvark'], 'c': ['coati'], 'b': ['baboon'], 'd': ['donkey', 'dog', 'dingo']}) # return 'd'
print biggest({}) # return None
# print biggest({'E': []}) # 'E'

# alternate
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result