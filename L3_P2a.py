l1, l2, l3, l4, l5 = [], [], [], [], []

# p1
print 2
print 4
print 6
print 8
print 10
print "Goodbye!"

# convert to while loop
x = 2
while x <= 10:
  print(x)
  x += 2
print("Goodbye!")

# p2
print "Hello!"
print 10
print 8
print 6
print 4
print 2

x = 10
print("Hello!")
while x >= 2:
  print(x)
  x -= 2

# p3
# Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we define end to be 6, your code should print out the result: 21
# which is 1 + 2 + 3 + 4 + 5 + 6

x = 1
y = 0 # total
end = 6
while x <= end:
  y += x
  x += 1
print(y)
