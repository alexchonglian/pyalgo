def quickSort(items):
    qs(items, 0, len(items)-1)

def qs(items, first, last):
    if first < last:
        pos = partition(items, first, last)
        qs(items, first, pos-1)
        qs(items, pos+1, last)

def partition(items, first, last):
    pivot = items[first]
    print('pivot', pivot, items)
    i,j = first+1, last
    while i < j:
        while i <= j and items[i] <= pivot:
            i += 1
        while i <= j and items[j] >= pivot:
            j -= 1
        if i < j:
            items[i], items[j] = items[j], items[i]
        print('  ', items[i], items[j], items)
    print(items, items[i], items[j], end=' ')
    #if items[i] < pivot:
    #    items[i], items[first] = items[first], items[i]
    #if items[j] > pivot:
    items[j], items[first] = items[first], items[j]
    print(items, items[i], items[j])
    return j

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
