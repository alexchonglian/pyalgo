class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next
	
	def __str__(self):
		return str(self.data) + '->' + str(self.next)
	
	def getNext(self):
		return self.next
	
	def setNext(self, next):
		self.next = next
	
	def getData(self):
		return self.data
	
	def setData(self, data):
		self.data = data

class OrderedList:
	def __init__(self, head):
		self.head = head

	def __str__(self):
		return str(self.head)

	def add(self, data):
		prev, curr = None, self.head
		while curr != None:
			prev, curr = curr, curr.next
		prev.next = Node(data)

	def remove(self, target):
		curr = self.head
		while curr.next != None and curr.next.data != target:
			curr = curr.next
		if curr.next == None:
			return
		if curr.next.next == None:
			curr.next = None
		else:
			curr.next, curr.next.next = curr.next.next, None

	def search(self, target):
		curr = self.head
		while curr.next != None:
			if curr.next.data == target:
				return True
			curr = curr.next
		return False

	def isEmpty(self):
		return self.head == None

	def size(self):
		count = 0
		curr = self.head
		while curr.next != None:
			count += 1
			curr = curr.next
		return count

	def index(target):
		count = 0
		curr = self.head
		while curr != None:
			if curr.data == target:
				return count
			count += 1
			curr = curr.next
		return -1

	def pop(self):
		pass

if __name__ == '__main__':
	N = Node
	o = OrderedList(N(1, N(2, N(3)))); print(o)
	o.add(4);print(o)
	o.add(5);print(o)
	o.remove(4);print(o)
	o.remove(5);print(o)



