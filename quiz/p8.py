# Problem 8
# (20 points possible)
# Write a Python function called satisfiesF that has the specification below. Then make the function call run_satisfiesF(L, satisfiesF). Your code should look like:

def f(s):
    return 'a' in s

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    clone = L[:]
    
    for item in clone:
        if not f(item):
            L.remove(item)
            
    return len(L)
    
def run_satisfiesF(L, satisfiesF):
    return satisfiesF(L)

L = ['a', 'b', 'a'] # return 2 for 'a'
# L = ['a', 'ba', 'b a b', 'c'] # return 3 for 'a'
# L = ['aa', 'b', 'a'] # return 2 for 'a' 
# L = ['a1', 'b', 'a'] # return 2 for 'a', 1 for '1'
print run_satisfiesF(L, satisfiesF)
# print satisfiesF(L)

# run_satisfiesF(L, satisfiesF)


# For your own testing of satisfiesF, for example, see the following test function f and test code:

# def f(s):
#     return 'a' in s
      
# L = ['a', 'b', 'a']
# print satisfiesF(L)
# print L

# # should print:
# # 2
# # ['a', 'a']

# Paste your entire function satisfiesF, including the definition, in the box below. After you define your function, make a function call to run_satisfiesF(L, satisfiesF). Do not define f or run_satisfiesF. Do not leave any debugging print statements.

# For this question, you will not be able to see the test cases we run. This problem will test your ability to come up with your own test cases.