# iterative function iterPower(base, exp) using successive multiplication

def iterPower(base, exp):
    '''
    base: int or float
    exp: int > 0
    
    returns: int or float, base^exp
    '''
#     result = base
#     if exp == 0:
#         result = 1

#     exp -= 1
#     while exp > 0:
#         exp -= 1
#         result *= base
#     return result
    
# ans = iterPower(2, 3)
# print(ans)

# v2: if exp == 0 then result will be one

    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result
    
ans = iterPower(2, 3)
print(ans)
ans2 = iterPower(2, 0)
print(ans2)
    