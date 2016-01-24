# counting vowels - 10pts
s = "azcbobobegghakl"
count = 0
for i in s:
    if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        count += 1
print "Number of vowels: {}".format(count)

# counting bobs - 15pts
""" there is a bobob """
bob = "bob"
count = 0
status = True
while status:
    if "bob" in s:
        count += 1
        s = s[s.index("bob") + 1:]
    else:
        status = False
print "Number of times bob occurs is: ", count

# counting and grouping - 15pts
def item_order(order):
    salad, hamburger, water = 0, 0, 0
    order = order.split(" ")
    for item in order:
        if item == "salad":
            salad += 1
        elif item == "hamburger":
            hamburger += 1
        elif item == "water":
            water += 1
    return "salad:{} hamburger:{} water:{}".format(salad, hamburger, water)
    
print item_order("salad water hamburger salad hamburger")