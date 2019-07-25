class ListNode:

	def __init__(self, value, NIL):
		self.value = value
		self.next = NIL

class LinkedList:

	def __init__(self):
		self.NIL = ListNode(0, 0)
		self.root = self.NIL
		self.last = self.NIL

	def append(self, value):
		newNode = ListNode(value, self.NIL)

		if (self.root == self.NIL):
			self.root = newNode

		if (self.last != self.NIL):
			self.last.next = newNode

		self.last = newNode

linkedList = LinkedList()

for i in range(0, 100):
	linkedList.append(i)

nextEntry = linkedList.root

while (nextEntry != linkedList.NIL):
	print(nextEntry.value)
	nextEntry = nextEntry.next
