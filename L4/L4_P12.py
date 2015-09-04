# default assignments
str1 = 'exterminate!'
str2 = 'number one - the larch'

# p1
print(str1.upper)

# p2
print(str1.upper())

# p3
print(str1)

# p4
print(str1.isupper())

# p5
print(str1.islower())

# p6
str2 = str2.capitalize() # Number one - the larch
print(str2)

# p7
print(str2.swapcase()) # nUMBER ONE - THE LARCH

# p8
print(str1.index('e'))

# p9
print(str2.index('n'))

# p10
print(str2.find('n'))

# p11
# print(str2.index('!')) # error

# p12
print(str2.find('!')) # -1

# p13
print(str1.count('e'))

# p14
str1 = str1.replace('e', '*') # *xt*rminat*!
print(str1)

# p15
print(str2.replace('one', 'seven'))


