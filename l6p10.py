aDict = {'a': ['aardvark'], 'c': ['coati'], 'b': ['baboon'], 'd': ['donkey', 'dog', 'dingo']}
def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
    # animals['d'] = ['donkey']
    # animals['d'].append('dog')
    # animals['d'].append('dingo')
    # print howMany(animals) # 6
    count = 0
    for value in aDict.values():
        count += len(value)
    return count
    
print howMany(aDict)

# alternate version
def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
    # animals['d'] = ['donkey']
    # animals['d'].append('dog')
    # animals['d'].append('dingo')
    # print howMany(animals) # 6
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result
    
print howMany(aDict)

