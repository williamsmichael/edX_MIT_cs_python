# Problem 4
# (10 points possible)
# Write a Python function that returns True if aString is a palindrome (reads the same forwards or reversed) and False otherwise. Do not use Python's built-in reverse function or aString[::-1] to reverse strings.

# This function takes in a string and returns a boolean.

def isPalindrome(aString):
    '''
    aString: a string
    '''
    # remove spaces and convert to lowercase
    aString = aString.replace(" ", "").lower()

    # reverse list
    rList = []
    for letter in aString:
    	rList.insert(0, letter)

    # break if false
    while True:
	    for i in range(len(aString)):
	    	return aString[i] == rList[i]
	    return True

# print isPalindrome("dad") # return True
print isPalindrome("papa") # return False
# print isPalindrome("nurses run") # return True
# print isPalindrome("madAM") # return True