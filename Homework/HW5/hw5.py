class LinkedList:
	def __init__(self,value=None):	
		self.value = value
	
	class Node:
		def __init__(self, value=None, next=None):
			self.value = value
			self.next = None
	
	def __str__(self):
		return str(self.value)
	
	def length(self):
		node = self.value
		i = 0
		if node.next != None:
			i += 1
			node = node.next
		return i
	
	def addNode(self,new_value):
		new_node = Node(new_value)
		if self.value == None:
			self.value = new_node
		else:
			self.value.next = new_node
	
	def addNodeAfter(self, new_value, after_node):
		to_add = Node(new_value)
		node = self_value
		i = 0
		if node.next != after_node:
			i += 1
			node = node.next
		elif node.next == after_node:
			# something
		else:
			# some error
	
	def addNodeBefore(self, new_value, before_node):
		to_add = Node(new_value)
		node = self_value
		i = 0
		if node.next != before_node:
			i += 1
			node = node.next
		elif node.next == before_node:
			# something
		else:
			# some error
	
	#def removeNode(self, node_to_remove):
	
	#def removeNodesByValue(self, value):
	
	#def reverse(self):
	
	#def __str(self)__:
	



