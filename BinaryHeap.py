class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.size = 0

    def percUp(self, i):
        while i > 1:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i],self.heapList[i//2] = self.heapList[i//2],self.heapList[i]
            i //= 2

    def insert(self, k):
        self.heapList.append(k)
        self.size += 1
        self.percUp(self.size)

    def percDown(self, i):
        while (i*2) <= self.size:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i],self.heapList[mc]=self.heapList[mc],self.heapList[i]
            i = mc
    
    def minChild(self, i):
        if i*2+1 > self.size:
            return i*2
        elif self.heapList[i*2] < self.heapList[i*2+1]:
            return i*2
        else:
            return i*2+1

    def getMin(self):
        return self.heapList[1]

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.size -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, items):
        i = len(items) // 2
        self.size = len(items)
        self.heapList = [0] + items[:]
        while i > 0:
            self.percDown(i)
            i -= 1

    def buildHeap2(self, items):
        for item in items:
            self.insert(item)

if __name__ == '__main__':
    from random import shuffle
    s = list(range(10000))
    shuffle(s)

    def f1():
        h1 = BinaryHeap()
        h1.buildHeap(s)
    
    def f2():
        h2 = BinaryHeap()
        h2.buildHeap2(s)

    import time
    start = time.time()
    for i in range(1000):f2()
    end = time.time()
    print(end - start)
