class Node:
	def __init__(self, key=None):
		self.key = key
		self.prev = self
		self.next = self
	def __str__(self):
		return str(self.key)

class DoublyLinkedList:
	def __init__(self):
		self.head = Node() # create an empty list with only dummy node

	def __iter__(self):
		v = self.head.next
		while v != self.head:
			yield v
			v = v.next
	def __str__(self):
		return " -> ".join(str(v.key) for v in self)

	def printList(self):
		v = self.head.next
		print("h -> ", end="")
		while v != self.head:
			print(str(v.key)+" -> ", end="")
			v = v.next
		print("h")
	# 나머지 코드
	def splice(self, a, b, x):
		if a == None or b == None or x == None:
			return
		a.prev.next = b.next
		b.next.prev = a.prev
		
		x.next.prev = b
		b.next = x.next
		a.prev = x
		x.next = a
		
	def moveAfter(self, a, x):
		self.splice(a, a, x)
		
	def moveBefore(self, a, x):
		self.splice(a, a, x.prev)
		
	def insertBefore(self, x, key):
		a = Node(key)
		self.moveBefore(a,x)
		
	def insertAfter(self, x, key):
		a = Node(key)
		self.moveAfter(a, x)
		
	def pushFront(self, key):
		x = self.head
		self.insertAfter(x, key)
		
	def pushBack(self, key):
		x = self.head
		self.insertBefore(x, key)
		
	def deleteNode(self, x):
		if x == None or x == self.head:
			return
		x.prev.next = x.next
		x.next.prev = x.prev
		del x
		
	def popFront(self):
		x = self.head.next
		key = x.key
		if key == 'h':
			return None
		else:
			self.deleteNode(x)
			return key
		
	def popBack(self):
		x = self.head.prev
		key = x.key
		if key == 'h':
			return None
		else:
			self.deleteNode(x)
			return key
		
	def search(self, key):
		v = self.head
		while v.next != self.head:
			if v.key == key:
				return v
			v = v.next
			
		if v.key == key:
			return v
		else:
			return None
		
	def first(self):
		if self.head.next.key == 'h':
			return None
		else:
			return self.head.next.key
		
	def last(self):
		if self.head.prev.key == 'h':
			return None
		else:
			return self.head.prev.key
		
	def isEmpty(self):
		if self.head.prev.key == 'h':
			return True
		else:
			return False
		
	def findMax(self):
		if self.head.next.key == 'h':
			return None
		
		else:
			v = self.head
			result = v.next.key
			while v.next != self.head:
				if v.next.key > result:
					result = v.next.key
				v = v.next
				
			return result
		
	def deleteMax(self):
		Max = self.findMax()
		v = self.search(Max)
		self.deleteNode(v)
		
		return Max
	
	def sort(self):
		list = []
		v = self.head
		while v.next != self.head:
			list.append(self.deleteMax())
		
		for i in range(0, len(list)):
			self.pushFront(list.pop(0))
			
		return self
	
L = DoublyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == 'pushF':
		L.pushFront(int(cmd[1]))
		print("+ {0} is pushed at Front".format(cmd[1]))
	elif cmd[0] == 'pushB':
		L.pushBack(int(cmd[1]))
		print("+ {0} is pushed at Back".format(cmd[1]))
	elif cmd[0] == 'popF':
		key = L.popFront()
		if key == None:
			print("* list is empty")
		else:
			print("- {0} is popped from Front".format(key))
	elif cmd[0] == 'popB':
		key = L.popBack()
		if key == None:
			print("* list is empty")
		else:
			print("- {0} is popped from Back".format(key))
	elif cmd[0] == 'search':
		v = L.search(int(cmd[1]))
		if v == None: print("* {0} is not found!".format(cmd[1]))
		else: print("* {0} is found!".format(cmd[1]))
	elif cmd[0] == 'insertA':
		# inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
		x = L.search(int(cmd[1]))
		if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
		else:
			L.insertAfter(x, int(cmd[2]))
			print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
	elif cmd[0] == 'insertB':
		# inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
		x = L.search(int(cmd[1]))
		if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
		else:
			L.insertBefore(x, int(cmd[2]))
			print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
	elif cmd[0] == 'delete':
		x = L.search(int(cmd[1]))
		if x == None:
			print("- {0} is not found, so nothing happens".format(cmd[1]))
		else:
			L.deleteNode(x)
			print("- {0} is deleted".format(cmd[1]))
	elif cmd[0] == "first":
		print("* {0} is the value at the front".format(L.first()))
	elif cmd[0] == "last":
		print("* {0} is the value at the back".format(L.last()))
	elif cmd[0] == "findMax":
		m = L.findMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key is", m)
	elif cmd[0] == "deleteMax":
		m = L.deleteMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key", m, "is deleted.")
	elif cmd[0] == 'sort':
		L = L.sort()
		L.printList()
	elif cmd[0] == 'print':
		L.printList()
	elif cmd[0] == 'exit':
		break
	else:
		print("* not allowed command. enter a proper command!")