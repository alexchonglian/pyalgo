class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

def check(stack, cmd, stat, val):
	retval = eval(cmd)
	assert retval == val
	assert stack.items == stat

if __name__ == '__main__':
	s = Stack()
	check(s, "s.isEmpty()", [], True)
	check(s, "s.push(4)", [4], None)
	check(s, "s.push('dog')", [4,'dog'], None)
	check(s, "s.peek()", [4,'dog'], 'dog')
	check(s, "s.push(True)", [4,'dog',True], None)
	check(s, "s.size()", [4,'dog',True], 3)
	check(s, "s.isEmpty()", [4,'dog',True], False)
	check(s, "s.push(8.4)", [4,'dog',True,8.4], None)
	check(s, "s.pop()", [4,'dog',True], 8.4)
	check(s, "s.pop()", [4,'dog'], True)
	check(s, "s.size()", [4,'dog'], 2)
