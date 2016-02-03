def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)

# -----------------------------------------------version 1
# def semordnilap(str1, str2):
#     '''
#     str1: a string
#     str2: a string
    
#     returns: True if str1 and str2 are semordnilap;
#              False otherwise.
#     '''
#     if len(str1) != len(str2):
#         return False
#     if (len(str1) == 1 and len(str2) == 1) and str1[0] == str2[0]:
#         return True
#     else:
#         return str1[0] == str2[-1] and semordnilap(str1[1:], str2[:-1])

# -----------------------------------------------version 2
def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # If strings aren't the same length, they cannot be semordnilap
    if len(str1) != len(str2):
        return False

    # Base case: if the strings are each of length 1, check if they're equal
    if len(str1) == 1:
        return str1 == str2

    # Recursive case: check if the first letter of str1 equals the last letter
    # of str2
    if str1[0] == str2[-1]:
        return semordnilap(str1[1:], str2[:-1])
    else:
        return False
        
print(semordnilapWrapper("nametag", "gateman"))
print(semordnilapWrapper("dog", "cat"))
print(semordnilapWrapper("live", "evil"))
print(semordnilapWrapper("desserts", "strissed"))

# -------------------------------------------set-up
# A semordnilap is a word or a phrase that spells a different word when backwards ("semordnilap" is a semordnilap of "palindromes"). Here are some examples:
# nametag / gateman
# dog / god
# live / evil
# desserts / stressed
    