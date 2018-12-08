def shell(items):
    count = len(items) // 2
    while count > 0:
        for startPos in range(count):
            gapInsert(items, startPos, count)
        count //= 2

def gapInsert(items, start, gap):
    for i in range(start+gap, len(items), gap):
        currVal = items[i]
        pos = i
        while pos >= gap and items[pos-gap] > currVal:
            items[pos] = items[pos-gap]
            pos -= gap
        items[pos] = currVal

alist = [54,26,93,17,77,31,44,55,20]
shell(alist)
print(alist)