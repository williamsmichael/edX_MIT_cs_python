# helpful comparison illustrating the need to clone or copy lists when traversing
# --------------------------------------------------------
def removeDups(L1, L2):
    for e1 in L1:
        print("at index:{}, e1 = {}".format(index, e1))
        if e1 in L2:
            L1.remove(e1)


L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDups(L1, L2)
print(L1)

def removeDupsBetter(L1, L2):
    index = 0
    L1Start = L1[:]
    for e1 in L1Start:
        print("at index:{}, e1 = {}".format(index, e1))
        if e1 in L2:
            L1.remove(e1)
        index += 1

L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDupsBetter(L1, L2)
print(L1)