def qs(items, start, end):
    if end <= start:
        return
    i, j = start + 1, end
    print(items, items[start])
    while i < j:
        while i <= j and items[i] <= items[start]:
            i += 1
        while i <= j and items[j] >= items[start]:
            j -= 1
        if i <= j:
            items[i], items[j] = items[j], items[i]
    items[start], items[j] = items[j], items[start]
    qs(items, start, j - 1)
    qs(items, j + 1, end)