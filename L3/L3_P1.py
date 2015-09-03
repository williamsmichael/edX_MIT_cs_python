list1 = []
num = 0
while num <= 5:
    list1.append(num)
    num += 1

list1.append("Outside of loop")
list1.append(num)
print(', '.join(map(str, list1)))


# numberOfLoops = 0
# numberOfApples = 2
# while numberOfLoops < 10:
#     numberOfApples *= 2
#     numberOfApples += numberOfLoops
#     numberOfLoops -= 1
# print "Number of apples: " + str(numberOfApples)
# Answer: infinite loop


list2 = []
num = 10
while num > 3:
    num -= 1
    list2.append(num)
print(', '.join(map(str, list2)))


list3 = []
num = 10
while True:
    if num < 7:
        list3.append('Breaking out of loop')
        break
    list3.append(num)
    num -= 1
list3.append('Outside of loop')
print(', '.join(map(str, list3)))


# list4 = []
# num = 100
# while not False:
#     if num < 0:
#         break
# list4.append('num is: ' + str(num))
# Answer: infinite loop
