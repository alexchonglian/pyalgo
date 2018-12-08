def bubble(items):
    for i in range(len(items)-1, 0, -1):
        for j in range(i):
            if items[j] > items[j+1]:
                items[j+1], items[j] = items[j], items[j+1]

alist = [54,26,93,17,77,31,44,55,20]
bubble(alist)
print(alist)