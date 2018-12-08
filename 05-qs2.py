def qs(items, start, end):
    if end <= start:
        return
    i,j = start+1,end
    print(items, items[start])
    while i < j:
        while i <= j and items[i] <= items[start]:
            i += 1
        while i <= j and items[j] >= items[start]:
            j -= 1
        if i <= j:
            items[i],items[j] = items[j],items[i]
    items[j], items[start] = items[start], items[j]

    qs(items, start, j-1)
    qs(items, j+1, end)

alist = [54,26,93,17,77,31,44,55,20]
qs(alist, 0, len(alist)-1)
print(alist)