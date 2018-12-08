def sb(items):
    ex = True
    n = len(items)-1
    while n > 0 and ex:
        ex = False
        for i in range(n):
            if items[i] > items[i+1]:
                ex = True
                items[i],items[i+1] = items[i+1],items[i]
        n -= 1

alist=[20,30,40,90,50,60,70,80,100,110]
sb(alist)
print(alist)