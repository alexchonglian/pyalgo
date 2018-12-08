def mergeSort(items):
    if len(items) <= 1:
        return
    mid = len(items) // 2
    left,right = items[:mid],items[mid:]
    mergeSort(left)
    mergeSort(right)
    i,j,k = 0,0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            items[k] = left[i]
            i += 1
        else:
            items[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        items[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        items[k] = right[j]
        j += 1
        k += 1

def mergeSort2(items):
    if len(items) <= 1:
        return items
    mid = len(items) //2

    left,right = mergeSort2(items[:mid]), mergeSort2(items[mid:])
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[-1] > right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()
    #print('res', res)
    if len(left) > 0: res = left + res
    if len(right) > 0: res = right + res
    return res

alist1 = [54,26,93,17,77,31,44,55,20]
mergeSort(alist1)
print(alist1)

alist2 = [54,26,93,17,77,31,44,55,20]
print(mergeSort2(alist2))
