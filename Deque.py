class Deque:
	def __init__(self):
		self.items = []

	def addFront(self, item):
		self.items.append(item)
		
	def addRear(self, item):
		self.items.insert(0, item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0)

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

def check(stack, cmd, stat, val):
	retval = eval(cmd)
	assert retval == val
	assert stack.items == stat

if __name__ == '__main__':
	d = Deque()
	check(d, "d.isEmpty()", [], True)
	check(d, "d.addRear(4)", [4], None)
	check(d, "d.addRear('dog')", ['dog',4,], None)
	check(d, "d.addFront('cat')", ['dog',4,'cat'], None)
	check(d, "d.addFront(True)", ['dog',4,'cat',True], None)
	check(d, "d.size()", ['dog',4,'cat',True], 4)
	check(d, "d.isEmpty()", ['dog',4,'cat',True], False)
	check(d, "d.addRear(8.4)", [8.4,'dog',4,'cat',True], None)
	check(d, "d.removeRear()", ['dog',4,'cat',True], 8.4)
	check(d, "d.removeFront()", ['dog',4,'cat'], True)
