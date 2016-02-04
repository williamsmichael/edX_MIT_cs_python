# For each of the following questions (which you may assume is evaluated independently of the previous questions, so that testList has the value indicated above), provide an expression using applyToEach, so that after evaluation testList has the indicated value. You may need to write a simple procedure in each question to help with this process.

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
testList = [1, -4, 8, -9]

# example
# >>> print testList [5, -20, 40, -45]

def timesFive(a):
    return a * 5

example = applyToEach(testList, timesFive)
print(example)

# # 7a
# # >>> print testList [1, 4, 8, 9]
# testList = [1, -4, 8, -9]

# def absolute(a):
#     if a < 0:
#         return a * -1
#     else:
#         return a
    
# applyToEach(testList, absolute)

# # alternate 7a
# applyToEach(testList, abs)

# # 7b
# testList = [1, -4, 8, -9]
# # >>> print testList [2, -3, 9, -8]

# def addOne(a):
#     return a + 1
        
# applyToEach(testList, addOne)

# 7c
testList = [1, -4, 8, -9]
# >>> print testList [1, 16, 64, 81]

def squared(a):
    return a * a
    
applyToEach(testList, squared)