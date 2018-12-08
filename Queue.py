class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

def check(queue, cmd, stat, val):
	retval = eval(cmd)
	#print( cmd, queue.items, stat, val, retval)
	assert retval == val
	assert queue.items == stat

if __name__ == '__main__':
	q = Queue()
	check(q, "q.isEmpty()", [], True)
	check(q, "q.enqueue(4)", [4], None)
	check(q, "q.enqueue('dog')", ['dog',4], None)
	check(q, "q.enqueue(True)", [True,'dog',4], None)
	check(q, "q.size()", [True,'dog',4], 3)
	check(q, "q.isEmpty()", [True,'dog',4], False)
	check(q, "q.enqueue(8.4)", [8.4,True,'dog',4], None)
	check(q, "q.dequeue()", [8.4,True,'dog'], 4)
	check(q, "q.dequeue()", [8.4,True], 'dog')
	check(q, "q.size()", [8.4,True], 2)