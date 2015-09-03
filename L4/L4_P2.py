
def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)

print(a(False, 2, 3)) # P1 answer 3
print(b(3, 2)) #P2 answer 3
print(a(3>2, a, b)) # P3 answer function
print(b(a, b))# P4 answer function
