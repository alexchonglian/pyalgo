def sel(items):
    for slot in range(len(items)-1, 0, -1):
        posMax = 0
        for i in range(1, slot+1):
            if items[i] > items[posMax]:
                posMax = i
        items[slot], items[posMax] = items[posMax], items[slot]

def sel2(items):
    for slot in range(0, len(items)):
        posMin = slot
        for i in range(slot+1, len(items)):
            if items[i] < items[posMin]:
                posMin = i
        items[slot], items[posMin] = items[posMin], items[slot]

l1 = [54,26,93,17,77,31,44,55,20]
sel(l1)
print(l1)

l2 = [54,26,93,17,77,31,44,55,20]
sel2(l2)
print(l2)