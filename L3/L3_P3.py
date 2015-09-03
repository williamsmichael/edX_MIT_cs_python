from collections import Counter
l1, l2, l3, l4, l5 = [], [], [], [], []

# p1
myStr = '6.00x'
for char in myStr:
    l1.append(char)
l1.append('done')
print(', '.join(map(str, l1)))
print(Counter(l1))
print([[x,l1.count(x)] for x in set(l1)])

# p2
greeting = 'Hello!'
count = 0
for letter in greeting:
    count += 1
    if count % 2 == 0:
        l2.append(letter)
    l2.append(letter)
l2.append('done')
print(', '.join(map(str, l2)))
print(Counter(l2))
print([[x,l2.count(x)] for x in set(l2)])

# p3
school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        l3.append(char)
    else:
        numCons -= 1

l3.append('numVowels is: ' + str(numVowels))
l3.append('numCons is: ' + str(numCons))
print(Counter(l3))
print([[x,l3.count(x)] for x in set(l3)])
