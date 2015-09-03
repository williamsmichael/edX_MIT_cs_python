# comparison
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step
        # print("inside while", guess, step)

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess) # the printout

# p1
# print("\n")
# x = 25
# epsilon = 0.01
# step = 0.1
# guess = 0.0
#
# the problem is when it hits 5, 5**2 - 25 is zero
# there exists no else so the loop is stuck
# while guess <= x:
#     if abs(guess**2 -x) >= epsilon:
#         guess += step
#         # print(guess, step)

# if abs(guess**2 - x) >= epsilon:
#     print 'failed'
# else:
#     print 'succeeded: ' + str(guess)


# p2 same as comparison
print("\n")
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)


# p3 changes x
print("\n")
x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
        # print(guess, step)
        # (22.900000000000055, 0.1)
        # (23.000000000000057, 0.1)
        # the jump above x breaks loop then fails below
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)

