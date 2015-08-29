# code sample to compare
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1

# p1 infinite loop
# print("\n")
# for iteration in range(5):
#     count = 0
#     while True:
#         for letter in "hello, world":
#             count += 1
#         print "Iteration " + str(iteration) + "; count is: " + str(count)

# p2 #different
print("\n")
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print "Iteration " + str(iteration) + "; count is: " + str(count)
        break


# p3 #same
print("\n")
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        # print(count, ": count")
        index += 1
        # print(index, ": index")
    print "Iteration " + str(iteration) + "; count is: " + str(count)


# p4 #same
print("\n")
count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print "Iteration " + str(iteration) + "; count is: " + str(count)


# p5
print("\n")
count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print "Iteration " + str(iteration) + "; count is: " + str(count)
