# bisection search to determine if a character is in a string, so long as the string is sorted in alphabetical order
# Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr. char will be a single character and aStr will be a string that is in alphabetical order. The function should return a boolean value.

def isIn(char, aStr):
    '''˜
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) <= 0:
        return False
    if len(aStr) == 1:
        return char == aStr
        
    midpoint = len(aStr) // 2
    if char == aStr[midpoint]:
        return True
    else: 
        if char < aStr[midpoint]:
            # print("lower")
            return isIn(char, aStr[:midpoint])
        else:
            # print("higher")
            return isIn(char, aStr[midpoint:])
    
print(isIn("o", ""))
print(isIn("o", "a"))
print(isIn('o', 'degmorrrstxxxyy'))
print(isIn('o', 'bfjo'))