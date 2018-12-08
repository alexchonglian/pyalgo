def insert(items):
    for i in range(1, len(items)):
        currVal = items[i]
        pos = i
        print(i, items, currVal, pos)
        while pos > 0 and items[pos-1] > currVal:
            items[pos] = items[pos-1]
            pos -= 1
        items[pos] = currVal

l = [54,26,93,17,77,31,44,55,20]
insert(l)
print(l)