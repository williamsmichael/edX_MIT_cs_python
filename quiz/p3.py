# Problem 3-1
# (2 points possible)
# Examine the following code snippet:

'''
stuff  = _____
  for thing in stuff:
        if thing == 'iQ':
           print "Found it"
'''

# stuff  = ( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], )
# for thing in stuff:
#     if thing == 'iQ':
#         print "Found it"

# Select all the values of the variable "stuff" that will make the code print "Found it".

# ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"]
# ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")
# [ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad") ]
# ( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], )
# ["iQ"]
# "iQ"

# ----------------------answer
# ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"]
# ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")
# ["iQ"]


# Problem 3-2
# (3 points possible)
# The following Python code is supposed to compute the square of an integer by using successive additions.

def Square(x):
	return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    # print n, x
    return SquareHelper(n-1, x) + x

# print Square(-4)

# Not considering recursion depth limitations, what is wrong with this implementation of procedure Square? Check all that apply.

# It is going to return a wrong value.
# The term Square is a reserved Python keyword.
# Function names cannot start with a capital letter.
# The function is never going to return anything.
# Python has arbitrary precision arithmetic.
# This function will not work for negative numbers.
# The call SquareHelper(abs(x), abs(x)) won't work because you can't have abs(x) as both parameters.
# Nothing is wrong; the code is fine as-is.

# ----------------------answer
# It is going to return a wrong value.
# This function will not work for negative numbers.