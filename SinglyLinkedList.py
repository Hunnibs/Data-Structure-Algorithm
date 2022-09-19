class Node:
	def __init__(self, key=None):
		self.key = key
		self.next = None
	def __str__(self):
		return str(self.key)
	
class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
	
	def __len__(self):
		return self.size
	
	def printList(self): # 변경없이 사용할 것!
		v = self.head
		while(v):
			print(v.key, "->", end=" ")
			v = v.next
		print("None")
	
	def pushFront(self, key):
		v = Node(key)
		v.next = self.head
		self.head = v
		self.size += 1
		
	def pushBack(self, key):
		v = Node(key)
		if self.size == 0:
			self.head = v
		else:
			tail = self.head
			while tail.next != None:
				tail = tail.next
			tail.next = v
		self.size += 1
		
	def popFront(self): 
		# head 노드의 값 리턴. empty list이면 None 리턴
		if self.size == 0:
			return None
		else:
			v = self.head
			key = v.key
			self.head = v.next
			self.size -= 1
			del v
			return key
	
	def popBack(self):
		# tail 노드의 값 리턴. empty list이면 None 리턴
		if self.size == 0:
			return None
		else:
			prev, tail = None, self.head
			while tail.next != None:
				prev = tail
				tail = tail.next
			if self.size == 1:
				self.head = None
			else:
				prev.next = tail.next
			key = tail.key
			del tail
			self.size -= 1
			return key
		
	def search(self, key):
		# key 값을 저장된 노드 리턴. 없으면 None 리턴
		v = self.head
		while v != None:
			if v.key == key:
				return v
			v = v.next
		return None
	
	def remove(self, x):
		# 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
		# x는 key 값이 아니라 노드임에 유의!
		if x == None:
			return False
		else:
			if x == self.head:
				if self.size == 1:
					self.head = None
				else:
					self.head = x.next
				del x
				self.size -= 1
				return True
				
			else:
				y = self.head
				while y.next != x:
					y = y.next
				y.next = x.next
				del x
				self.size -= 1
				return True
			
	def reverse(self, key):
		count = 0
		v = self.head
		while v != None:
			if v.key == key:
				break
			v = v.next
			count += 1
		
		if v == None or v.next == None:
			return None
		
		for i in range(count, self.size-1):
			x = v
			while x.next != None:
				x = x.next
			self.insert(i, x.key)
			self.popBack()
		
	def findMax(self):
		# self가 empty이면 None, 아니면 max key 리턴
		if self.size == 0:
			return None
		
		else:
			x = self.head
			y = self.size
			for i in range(0, y):
				key = x.key
				self.pushBack(key)
				x = x.next
				
			for i in range(0,y-1):
				x = self.head
				a = x.next
				key2 = x.key
				key3 = a.key
				if key2 <= key3:
					self.popFront()
				else:
					self.insert(2, key2)
					self.popFront()
					self.popFront()
				
			result = self.head.key
			self.popFront()
			
			return result
				
	def deleteMax(self):
		# self가 empty이면 None, 아니면 max key 지운 후, max key 리턴
		if self.size == 0:
			return None
		else:
			if self.size == 1:
				key_Max = self.head.key
				self.head = None
				self.size -= 1
			else:
				key_Max = self.findMax()
				while key_Max == self.findMax():
					v = self.search(key_Max)
					self.remove(v)
			return key_Max
			
	def insert(self, k, val):
		if self.size < k:
			self.pushBack(val)
		else:
			for i in range(0, k):
				key1 = self.head.key
				self.pushBack(key1)
				self.popFront()
			self.pushFront(val)
			for i in range(0, k):
				x = self.head
				while x.next != None:
					x = x.next
				key2 = x.key
				self.pushFront(key2)
				self.popBack()
			
	def size(self):
		return self.size
	
# 아래 코드는 수정하지 마세요!
L = SinglyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == "pushFront":
		L.pushFront(int(cmd[1]))
		print(int(cmd[1]), "is pushed at front.")
	elif cmd[0] == "pushBack":
		L.pushBack(int(cmd[1]))
		print(int(cmd[1]), "is pushed at back.")
	elif cmd[0] == "popFront":
		x = L.popFront()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from front.")
	elif cmd[0] == "popBack":
		x = L.popBack()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from back.")
	elif cmd[0] == "search":
		x = L.search(int(cmd[1]))
		if x == None:
			print(int(cmd[1]), "is not found!")
		else:
			print(int(cmd[1]), "is found!")
	elif cmd[0] == "remove":
		x = L.search(int(cmd[1]))
		if L.remove(x):
			print(x.key, "is removed.")
		else:
			print("Key is not removed for some reason.")
	elif cmd[0] == "reverse":
		L.reverse(int(cmd[1]))
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
	elif cmd[0] == "insert":
		L.insert(int(cmd[1]), int(cmd[2]))
		print(cmd[2], "is inserted at", cmd[1]+"-th position.")
	elif cmd[0] == "printList":
		L.printList()
	elif cmd[0] == "size":
		print("list has", len(L), "nodes.")
	elif cmd[0] == "exit":
		print("DONE!")
		break
	else:
		print("Not allowed operation! Enter a legal one!")