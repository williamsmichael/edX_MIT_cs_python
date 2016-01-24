p1, p2, p3, p4, p5 = [], [], [], [], []


# p1
num = 10
for num in range(5):
    p1.append(num)
p1.append(num)
print(', '.join(map(str, p1)))

# p2
divisor = 2
for num in range(0, 10, 2):
    p2.append(num/divisor)
print(', '.join(map(str, p2)))

# p3
for variable in range(20):
    if variable % 4 == 0:
        p3.append(variable)
    if variable % 16 == 0:
        p3.append('Foo!') # 0, 16
print(', '.join(map(str, p3)))

# p4
for letter in 'hola':
    p4.append(letter)
print(', '.join(map(str, p4)))

# p5
count = 0
for letter in 'Snow!':
    p5.append('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
p5.append(count)
print(', '.join(map(str, p5)))

