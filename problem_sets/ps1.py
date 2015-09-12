"""
Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""

# vowels count = 59
s = "supports three forms of initialization. Its constructor can be called with a sequence of items, a dictionary containing keys and counts, or using keyword arguments mapping string names to counts"

vowels = list('aeiou')
total = 0
for each_vowel in vowels:
  total += s.count(each_vowel)
print("Number of vowels: {}".format(total))


"""
Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2

>>> situation: overlapping sequences of substrings
"""

s = 'azcbobobegghabobobobkl' # 5 occurences
bob = 'bob'
total = 0
startIndex = 0

# .find Index if found and -1 otherwise
# go through each index of the string s
while startIndex < len(s):
  index_found = s.find(bob, startIndex)
  # print("index found: ", index_found)
  if index_found >= 0:
    total += 1
    startIndex = index_found + 1 # reset the startIndex
    # print("total: ", total)
    # print("startIndex: ", startIndex)
  else:
    startIndex = len(s)
    # print(startIndex)
    # print(len(s))

print("Number of times bob occurs is: {}".format(total))


"""
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

# s = 'azcbobobegghakl'
start = 0
iterator = 0
finish = 1
subStr = ""
subStrFinal = ""


while finish < len(s):
  if s[iterator] <= s[finish]:
    subStr = s[start:finish + 1]
    iterator += 1
    finish += 1
    # print(start, iterator, finish)
  else:
    if len(subStr) > len(subStrFinal):
      subStrFinal = subStr
    start = finish
    iterator = finish
    finish += 1
    # print(start, iterator, finish)
print("Longest substring in alphabetical order is: {}".format(subStrFinal))













