WORDLIST_FILENAME = "words.txt"
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList
    
def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    status = []
    status2 = []

    # check if the input is valid
    if not word in wordList:
        return False
        
    for letter in word:
        
        ## commented out bc global var not available for the individual exercise
        # if not letter in SCRABBLE_LETTER_VALUES.keys():
        #     status.append(False)
            
        if not letter in hand.keys():
            status.append(False)
            
    if False in status:
        return False
    
    # check if there are enough values in hand for the guess
    for key, value in getFrequencyDict(word).items():
        
        if not key in hand or value > hand[key]:
            status2.append(False)

    if False in status2:
        return False
    
    return True
            
    
word = "yummy"
hand = {'y':1, 'u':1, 'm':4}
wordList = loadWords()
print isValidWord(word, hand, wordList)