# for loops

# p1
print 2
print 4
print 6
print 8
print 10
print "Goodbye!"

for i in range(2, 11, 2):
  print(i)
print("Goodbye!")

# p2
print "Hello!"
print 10
print 8
print 6
print 4
print 2

print("Hello!")
for i in range(10, 1, -2):
  print(i)

print("\n")
# p3
# Write a for loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we define end to be 6, your code should print out the result: 21
# which is 1 + 2 + 3 + 4 + 5 + 6

end = 6
current = 1
total = 0
for num in range(current, end + 1):
  total += current
  current += 1
print(total)

