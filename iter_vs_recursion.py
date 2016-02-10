# ----------------------------------------multiplication
# iterative
def iterMul(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

# factorial
def recurMul(a, b):
    if b == 1:
        # if you are in the base case, just return that value
        return a
    else:
        return a + recurMul(a, b-1)

# ----------------------------------------factorial
# iterative
def factI_whileLoop(n):
    """assumes that n is an int > 0
       returns n!"""
    res = 1
    while n > 1:
        res = res * n
        n -= 1
    return res
    
def factI_forLoop(n):
    res = 1
    for i in range(n):
        res *= (i + 1)
    return res
        
# recursion
def factR(n):
    """assumes that n is an int > 0
       returns n!"""
    if n == 1:
        # if you are in the base case, just return that value
        return n
    return n * factR(n - 1)
# print(factR(6))
    
# ----------------------------------------fibonacci
# Example 1: Using looping technique
def fib_forLoop(n):
 a, b = 1, 1
 for i in range(n-1):
  a, b = b, a + b
 return a
# print(fib_forLoop(6))

def fib_whileLoop(n):
    terms = [0, 1]
    i = 2
    while i <= n:
        terms.append(terms[i-1] + terms[i-2])
        i += 1
    return terms[n]
# print fib_whileLoop(6)

# recursion
def fibR(x):
    """assumes x an int >= 0
      returns Fibonacci of x"""
    assert type(x) == int and x >= 0
    # if x == 0 or x == 1:
    #     return 1
    if x < 2:
        return x
    else:
        # print fibR(x-1) + fibR(x-2)
        return fibR(x-1) + fibR(x-2)
print fibR(6)

    